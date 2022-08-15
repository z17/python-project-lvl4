from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from django.views.generic import CreateView, DeleteView, UpdateView, ListView

from task_manager.users.models import UserForm
from django.contrib.auth.models import User


class UserListView(ListView):
    model = User
    template_name = 'users/users.html'


class UsersCreateView(CreateView):
    form_class = UserForm
    template_name = 'users/users_create.html'
    success_url = '/users/login'


class UsersUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'users/users_update.html'
    success_url = '/users/'

    def dispatch(self, request, *args, **kwargs):
        if request.user != self.get_object():
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class UsersDeleteView(DeleteView):
    model = User
    template_name = 'users/users_delete.html'
    success_url = '/users/'

    def dispatch(self, request, *args, **kwargs):
        if request.user != self.get_object():
            return self.handle_no_permission()
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
