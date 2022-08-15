from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy

from task_manager.labels.models import Label


class LabelListView(LoginRequiredMixin, ListView):
    model = Label
    template_name = 'labels/label_list.html'


class LabelCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Label
    fields = ['name']
    template_name = 'labels/label_create.html'
    success_url = reverse_lazy('labels:index')
    success_message = _('Label created')


class LabelUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Label
    fields = ['name']
    template_name = 'labels/label_update.html'
    success_url = reverse_lazy('labels:index')
    success_message = _('Label updated')


class LabelDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Label
    template_name = 'labels/label_delete.html'
    success_url = reverse_lazy('labels:index')
    success_message = _('Label deleted')
