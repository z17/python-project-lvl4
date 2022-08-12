from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render

from django.views.generic import CreateView, DeleteView, UpdateView

from task_manager.users.models import UserCreationForm


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
