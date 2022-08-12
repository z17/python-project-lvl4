from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse

from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView

from task_manager.models import Task, Status, Label
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

    def dispatch(self, request, *args, **kwargs):
        if request.user != self.get_object():
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class UsersDeleteView(DeleteView):
    model = get_user_model()
    template_name = 'users_delete.html'
    success_url = '/users/'

    def dispatch(self, request, *args, **kwargs):
        if request.user != self.get_object():
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


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


class TaskView(DetailView):
    model = Task

    template_name = 'task_detail.html'


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['name', 'status', 'text', 'assignee', 'labels']
    template_name = 'task_create.html'

    def form_valid(self, form):
        user = self.request.user
        form.instance.reporter = user
        return super(TaskCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('task', args=(self.object.id,))


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['name', 'status', 'text', 'assignee', 'labels']
    template_name = 'task_update.html'

    def form_valid(self, form):
        user = self.request.user
        form.instance.reporter = user
        return super(TaskUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('task', args=(self.object.id,))


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task_delete.html'
    success_url = '/tasks/'

    def dispatch(self, request, *args, **kwargs):
        if request.user != self.get_object().reporter:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class LabelListView(LoginRequiredMixin, ListView):
    model = Label
    template_name = 'label_list.html'


class LabelCreateView(LoginRequiredMixin, CreateView):
    model = Label
    fields = ['name']
    template_name = 'label_create.html'
    success_url = '/labels/'


class LabelUpdateView(LoginRequiredMixin, UpdateView):
    model = Label
    fields = ['name']
    template_name = 'label_update.html'
    success_url = '/labels/'


class LabelDeleteView(LoginRequiredMixin, DeleteView):
    model = Label
    template_name = 'label_delete.html'
    success_url = '/labels/'
