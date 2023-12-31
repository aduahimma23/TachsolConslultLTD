# accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    staff_id = forms.CharField(max_length=10, required=True)

    class Meta:
        model = CustomUser
        fields = ('staff_id', 'password1', 'password2')

class LoginForm(forms.Form):
    staff_id = forms.CharField(max_length=10, required=True)
    password = forms.CharField(widget=forms.PasswordInput)
