from django.urls import path
from . import views


urlpatterns = [
    path('', views.forum_home, name="forum_home"),
    path('create', views.create, name="create"),
    path('<int:pk>', views.ForumDetailView.as_view(), name="forum_detail")
]
