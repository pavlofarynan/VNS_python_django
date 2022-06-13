from django.urls import path
from . import views


urlpatterns = [
    path('', views.forum_home, name="forum_home"),
    path('create', views.forum_create, name="create"),
]