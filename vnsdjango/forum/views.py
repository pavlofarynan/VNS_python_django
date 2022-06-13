from django.shortcuts import render, redirect
from .models import Forum
from .forms import ForumForm
from django.views.generic import DetailView, UpdateView, DeleteView


def forum_home(request):
    forum = Forum.objects.order_by('-date')
    return render(request, 'forum/forum_home.html', {'forum': forum})


class ForumDetailView(DetailView):
    model = Forum
    template_name = 'forum/details_view.html'
    context_object_name = 'post'


class ForumUpdateView(UpdateView):
    model = Forum
    template_name = 'forum/create.html'
    #fields = ['title', 'anons', 'full_text', 'date']
    form_class = ForumForm


class ForumDeleteView(DeleteView):
    model = Forum
    template_name = 'forum/forum_delete.html'
    success_url = '/forum/'


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
