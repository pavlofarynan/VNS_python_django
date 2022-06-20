from django import forms
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="Username", help_text="Your username must consist maximum with 150 symbols", widget=forms.TextInput(attrs={
                'class': 'form-control'}))
    first_name = forms.CharField(label="First name", widget=forms.TextInput(attrs={
        'class': 'form-control'}))
    last_name = forms.CharField(label="Last name", widget=forms.TextInput(attrs={
        'class': 'form-control'}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={
        'class': 'form-control'}))
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput(attrs={
        'class': 'form-control'}))
    email = forms.EmailField(label="E-mail", widget=forms.EmailInput(attrs={
        'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
