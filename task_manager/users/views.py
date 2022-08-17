from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from django.views.generic import CreateView, DeleteView, UpdateView, ListView

from task_manager.users.models import UserForm, User


class UserListView(ListView):
    model = User
    template_name = 'users/users.html'


class UsersCreateView(SuccessMessageMixin, CreateView):
    form_class = UserForm
    template_name = 'users/users_create.html'
    success_url = reverse_lazy('login')
    success_message = _('User successfully registered')


class UsersUpdateView(SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'users/users_update.html'
    success_url = reverse_lazy('users:index')
    success_message = _('User successfully updated')

    def dispatch(self, request, *args, **kwargs):
        if request.user.id != self.get_object().id:
            messages.error(self.request, _('You do not have permission to modify another user.'))
            return redirect(reverse_lazy('users:index'))

        return super().dispatch(request, *args, **kwargs)


class UsersDeleteView(SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'users/users_delete.html'
    success_url = reverse_lazy('users:index')
    success_message = _('User successfully deleted')

    def dispatch(self, request, *args, **kwargs):
        if request.user.id != self.get_object().id:
            messages.error(self.request, _('You do not have permission to modify another user.'))
            return redirect(reverse_lazy('users:index'))
        return super().dispatch(request, *args, **kwargs)


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'users/users_login.html'
    next_page = reverse_lazy('index')
    success_message = _('You are logged in')


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.info(request, _('You are logged out'))
        return response
