from django.shortcuts import render, redirect
from .models import SignIn
from .forms import SigninForm
# Create your views here.


def signin(request):
    error = ''
    if request.method == "POST":
        sign_in = SigninForm(request.POST)
        if sign_in.is_valid():
            sign_in.save()
            return redirect('home')
        else:
            error = "Wrong data!"
    sign_in = SigninForm()
    data = {
        'signin': sign_in
    }

    return render(request, 'signin/signin.html', data)
