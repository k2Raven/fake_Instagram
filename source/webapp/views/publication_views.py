from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
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
