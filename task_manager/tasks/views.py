
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django_filters import FilterSet, BooleanFilter
from django.utils.translation import gettext_lazy as _
from django_filters.views import FilterView
from django import forms

from task_manager.tasks.models import Task


class TaskFilter(FilterSet):
    created_by_me = BooleanFilter(
        field_name='creator',
        label=_('Created by me'),
        widget=forms.CheckboxInput,
        method='filter_self_tasks',

    )

    def filter_self_tasks(self, queryset, name, value):
        if not value:
            return queryset

        return queryset.filter(reporter=self.request.user)

    class Meta:
        model = Task

        fields = ['status', 'assignee', 'labels', 'created_by_me']


class TaskListView(LoginRequiredMixin, FilterView):
    model = Task
    template_name = 'tasks/tasks_list.html'
    filterset_class = TaskFilter


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
