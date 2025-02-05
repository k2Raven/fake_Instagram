from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, ListView

from webapp.forms.publication import PublicationForm
from webapp.models import Publication


class PublicationListView(LoginRequiredMixin, ListView):
    model = Publication
    context_object_name = 'publications'
    template_name = 'publication/list.html'

    def get_queryset(self):
        subscriptions = self.request.user.subscriptions.all()
        return Publication.objects.filter(author__in=subscriptions).order_by('-created_at')


class PublicationCreateView(LoginRequiredMixin, CreateView):
    model = Publication
    form_class = PublicationForm
    template_name = 'publication/create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accounts:profile', kwargs={'pk': self.request.user.id})


class LikePublicationView(LoginRequiredMixin, View):
    def get(self, request, *args, pk, **kwargs):
        publication = get_object_or_404(Publication, pk=pk)
        if request.user in publication.users_liked.all():
            publication.users_liked.remove(request.user)
            publication.likes_counter -= 1
            publication.save()
        else:
            publication.users_liked.add(request.user)
            publication.likes_counter += 1
            publication.save()
        return redirect('webapp:publication-list')
