from .models import SignIn
from django.forms import ModelForm, TextInput


class SigninForm(ModelForm):
    class Meta:
        model = SignIn
        fields = ['name', 'surname', 'mail', 'password']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'User name'
            }),
            'surname': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'User surname'
            }),
            'mail': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'User email'
            }),
            'password': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'User password',
            })
        }
