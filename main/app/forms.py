from django import forms

from django.contrib.auth.forms import UserCreationForm
from  .models import*

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'password1', 'password2']