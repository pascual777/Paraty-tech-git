from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=150, help_text='Enter a username. Only letters, digits, and @/./+/-/_ are allowed.')

    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def clean_username(self):
        username = self.cleaned_data['username']
        return username.replace(' ', '_')


