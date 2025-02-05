from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import widgets


User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'avatar', 'password1', 'password2', 'first_name', 'last_name', 'user_info', 'phone_number', 'gender')


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class SearchUserForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Поиск', widget=widgets.TextInput(attrs={'class': 'form-control'}))
