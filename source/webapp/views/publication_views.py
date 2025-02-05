from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView

from webapp.forms.publication import PublicationForm
from webapp.models import Publication


class PublicationListView(View):
    def get(self, request):
        return render(request, 'publication/list.html')

class PublicationCreateView(LoginRequiredMixin, CreateView):
    model = Publication
    form_class = PublicationForm
    template_name = 'publication/create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accounts:profile', kwargs={'pk': self.request.user.id})
