from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('role', 'age')


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        models = CustomUser
        fields = UserChangeForm.Meta.fields