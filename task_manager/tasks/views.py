from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django_filters import FilterSet, BooleanFilter, ModelChoiceFilter
from django.utils.translation import gettext_lazy as _
from django_filters.views import FilterView
from django import forms

from task_manager.labels.models import Label
from task_manager.tasks.models import Task
from task_manager.users.models import User


class TaskFilter(FilterSet):
    created_by_me = BooleanFilter(
        field_name='creator',
        label=_('Created by me'),
        widget=forms.CheckboxInput,
        method='filter_self_tasks',

    )

    label = ModelChoiceFilter(
        queryset=Label.objects.all(),
        field_name='labels',
        label=_('Label'),
    )

    def filter_self_tasks(self, queryset, name, value):
        if not value:
            return queryset

        return queryset.filter(reporter=self.request.user)

    class Meta:
        model = Task

        fields = ['status', 'executor', 'label', 'created_by_me']


class TaskListView(LoginRequiredMixin, FilterView):
    model = Task
    template_name = 'tasks/tasks_list.html'
    filterset_class = TaskFilter


class TaskView(DetailView):
    model = Task

    template_name = 'tasks/task_detail.html'


class TaskCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Task
    fields = ['name', 'status', 'description', 'executor', 'labels']
    template_name = 'tasks/task_create.html'
    success_message = _('Task created')
    success_url = reverse_lazy('tasks:index')

    def form_valid(self, form):
        user = self.request.user
        form.instance.reporter = User.objects.get(id=user.id)
        return super(TaskCreateView, self).form_valid(form)


class TaskUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Task
    fields = ['name', 'status', 'description', 'executor', 'labels']
    template_name = 'tasks/task_update.html'
    success_message = _('Task updated')
    success_url = reverse_lazy('tasks:index')


class TaskDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Task
    template_name = 'tasks/task_delete.html'
    success_url = reverse_lazy('tasks:index')
    success_message = _('Task deleted')

    def dispatch(self, request, *args, **kwargs):
        if request.user != self.get_object().reporter:
            messages.error(self.request, _('Access denied'))
            return redirect(reverse_lazy('index'))
        return super().dispatch(request, *args, **kwargs)
