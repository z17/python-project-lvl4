from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render

from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView

from task_manager.models import Task, Status
from task_manager.users import UserCreationForm


def index(request):
    return render(request, 'index.html', context={
        'who': 'World',
    })


def users(request):
    all_users = User.objects.order_by(
        'id'
    )

    return render(request, 'users.html', context={
        'users': all_users
    })


class UsersCreateView(CreateView):
    form_class = UserCreationForm
    template_name = 'users_create.html'
    success_url = '/users/login'


class UsersUpdateView(UpdateView):
    model = get_user_model()
    form_class = UserCreationForm
    template_name = 'users_update.html'
    success_url = '/users/'


class UsersDeleteView(DeleteView):
    model = get_user_model()
    template_name = 'users_delete.html'
    success_url = '/users/'


class UserLoginView(LoginView):
    template_name = 'users_login.html'


class UserLogoutView(LogoutView):
    next_page = '/'


class StatusListView(LoginRequiredMixin, ListView):
    model = Status
    template_name = 'status_list.html'


class StatusCreateView(LoginRequiredMixin, CreateView):
    model = Status
    fields = ['name']
    template_name = 'status_create.html'
    success_url = '/statuses/'


class StatusUpdateView(LoginRequiredMixin, UpdateView):
    model = Status
    fields = ['name']
    template_name = 'status_update.html'
    success_url = '/statuses/'


class StatusDeleteView(LoginRequiredMixin, DeleteView):
    model = Status
    template_name = 'status_delete.html'
    success_url = '/statuses/'


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks_list.html'


class TaskView(LoginRequiredMixin, DetailView):
    model = Task


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
