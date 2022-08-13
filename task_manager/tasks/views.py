from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from task_manager.tasks.models import Task


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/tasks_list.html'


class TaskView(DetailView):
    model = Task

    template_name = 'tasks/task_detail.html'


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['name', 'status', 'text', 'assignee', 'labels']
    template_name = 'tasks/task_create.html'

    def form_valid(self, form):
        user = self.request.user
        form.instance.reporter = user
        return super(TaskCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('task', args=(self.object.id,))


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['name', 'status', 'text', 'assignee', 'labels']
    template_name = 'tasks/task_update.html'

    def form_valid(self, form):
        user = self.request.user
        form.instance.reporter = user
        return super(TaskUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('task', args=(self.object.id,))


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/task_delete.html'
    success_url = '/tasks/'

    def dispatch(self, request, *args, **kwargs):
        if request.user != self.get_object().reporter:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
