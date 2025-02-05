from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms


User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'avatar', 'password1', 'password2', 'first_name', 'last_name', 'user_info', 'phone_number', 'gender')


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
