from django.shortcuts import render, redirect
from .models import Forum
from .forms import ForumForm
# Create your views here.


def forum_home(request):
    forum = Forum.objects.order_by('-date')
    return render(request, 'forum/forum_home.html', {'forum': forum})


def create(request):
    error = ''
    if request.method == "POST":
        form = ForumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Wrong data in post"
    form = ForumForm()
    data = {
        'form': form
    }

    return render(request, 'forum/create.html', data)