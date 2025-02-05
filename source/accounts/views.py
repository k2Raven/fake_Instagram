from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, reverse
from django.views.generic import CreateView, DetailView, UpdateView

from accounts.forms import CustomUserCreationForm, UserChangeForm

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
        # reviews = Review.objects.filter(auther=self.object)
        # if not self.request.user.has_perm('webapp.see_all_reviews') and not self.object == self.request.user:
        #     reviews = reviews.filter(is_moderated=True)
        # context['reviews'] = reviews
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
