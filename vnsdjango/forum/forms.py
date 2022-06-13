from .models import Forum
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ForumForm(ModelForm):
    class Meta:
        model = Forum
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name of the post'
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Anons post'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Text of the post'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date of publishing',
                'type': 'date',
            })
        }