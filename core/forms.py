from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, EmailInput, FileInput, Textarea

from .models import UserProfile


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'address', 'city',
                  'estate', 'postal_code', 'about', 'avatar']

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'address': TextInput(attrs={'class': 'form-control'}),
            'city': TextInput(attrs={'class': 'form-control'}),
            'estate': TextInput(attrs={'class': 'form-control'}),
            'postal_code': TextInput(attrs={'class': 'form-control'}),
            'about': Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'avatar': FileInput(attrs={'class': 'form-control'}),
        }


class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

        widgets = {
            'first_name': TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'last_name': TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Sobrenome'}),
            'email': EmailInput(
                attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }
