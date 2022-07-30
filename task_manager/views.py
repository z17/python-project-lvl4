from django.contrib.auth.models import User
from django.shortcuts import render

from django.views.generic import CreateView

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
    success_url = '/users/'
