from django.urls import path
from task_manager.users import views

app_name = 'users'

urlpatterns = [
    path('', views.users),
    path('create/', views.UsersCreateView.as_view(), name='create'),
    path('<pk>/update/', views.UsersUpdateView.as_view()),
    path('<pk>/delete/', views.UsersDeleteView.as_view()),
]
