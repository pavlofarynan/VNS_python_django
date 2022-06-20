from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
# Create your views here.


def register(request):
    template_name = 'user_control/registration.html'
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nicely done!')
            return redirect('registration')
        else:
            messages.error(request, "smth wrong")
    else:
        form = UserRegisterForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)


class LoginView(TemplateView):
    template_name = 'user_control/login.html'
    context_object_name = 'post'

    def get(self, request):
        return render(request, self.template_name, {})