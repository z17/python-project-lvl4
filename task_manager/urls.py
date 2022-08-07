"""task_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task_manager import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),

    path('users/', views.users),
    path('users/create/', views.UsersCreateView.as_view()),
    path('users/<pk>/update/', views.UsersUpdateView.as_view()),
    path('users/<pk>/delete/', views.UsersDeleteView.as_view()),
    path('users/login/', views.UserLoginView.as_view()),
    path('users/logout/', views.UserLogoutView.as_view()),

    path('statuses/', views.StatusListView.as_view()),
    path('statuses/create/', views.StatusCreateView.as_view()),
    path('statuses/<pk>/update/', views.StatusUpdateView.as_view()),
    path('statuses/<pk>/delete/', views.StatusDeleteView.as_view()),

    path('tasks/', views.TaskListView.as_view()),
    path('tasks/create/', views.TaskCreateView.as_view()),
    path('tasks/<pk>/update/', views.TaskUpdateView.as_view()),
    path('tasks/<pk>/delete/', views.TaskDeleteView.as_view()),
    path('tasks/<pk>/', views.TaskView.as_view(), name='task'),
]
