from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm
# Create your views here.


def register(request):
    template_name = 'user_control/registration.html'
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Nicely done!')
            return redirect('home')
        else:
            messages.error(request, "smth wrong")
    else:
        form = UserRegisterForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)


def user_login(request):
    template_name = 'user_control/login.html'
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    context = {"form": form}
    return render(request, template_name, context)


def user_logout(request):
    logout(request)
    return redirect('login')
