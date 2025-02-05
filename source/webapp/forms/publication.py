from django import forms

from webapp.models import Publication


class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['picture','description']