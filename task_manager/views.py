from django.contrib.auth.models import User
from django.shortcuts import render


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
