from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import CreateView
from django.contrib import messages

from webapp.forms.comment import CommentForm
from webapp.models import Comment, Publication


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        return reverse('webapp:publication-detail', kwargs={'pk': self.publication.pk})

    def dispatch(self, request, *args, **kwargs):
        self.publication = get_object_or_404(Publication, pk=kwargs.get('pk'))
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.publication = self.publication
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error ')
        return redirect(self.get_success_url())