from django.db.models import Q

from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import redirect, reverse, get_object_or_404
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView, TemplateView

from accounts.forms import CustomUserCreationForm, UserChangeForm, SearchUserForm
from webapp.models import Publication

User = get_user_model()


class RegisterView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'registration.html'

    def form_valid(self, form):
        self.object = form.save()
        login(self.request, self.object)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('webapp:articles')
        return next_url


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'

    # paginate_related_by = 3
    # paginate_related_orphans = 0

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        publications = Publication.objects.filter(author=self.object).order_by('-created_at')
        context['publications'] = publications
        return context


class UserChangeView(UserPassesTestMixin, UpdateView):
    model = User
    form_class = UserChangeForm
    template_name = 'user_change.html'
    context_object_name = 'user_obj'

    def test_func(self):
        return self.request.user == self.get_object()

    def get_success_url(self):
        return reverse('accounts:profile', kwargs={'pk': self.object.pk})


class UserPasswordChangeView(PasswordChangeView):
    template_name = 'user_password_change.html'

    def get_success_url(self):
        return reverse('accounts:profile', kwargs={'pk': self.request.user.pk})



class SearchUsersView(TemplateView):
    template_name = 'search_users.html'

    def get_search_form(self):
        return SearchUserForm(self.request.GET)

    def get_search_value(self):
        if self.search_form.is_valid():
            return self.search_form.cleaned_data['search']

    def dispatch(self, request, *args, **kwargs):
        self.search_form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.search_form
        if self.search_value:
            context['users'] = User.objects.filter(
                Q(first_name__icontains=self.search_value) |
                Q(last_name__icontains=self.search_value) |
                Q(email__icontains=self.search_value) |
                Q(username__icontains=self.search_value)
            )
        return context

class SubscriptionView(LoginRequiredMixin, View):
    def get(self, request, *args, pk, **kwargs):
        user = get_object_or_404(User, pk=pk)
        if user != request.user:
            if request.user in user.followers.all():
                user.followers.remove(request.user)
                user.followers_count -= 1
                user.save()
                request.user.subscriptions_count -= 1
                request.user.save()
            else:
                user.followers.add(request.user)
                user.followers_count += 1
                user.save()
                request.user.subscriptions_count += 1
                request.user.save()
        return redirect('webapp:publication-list')
