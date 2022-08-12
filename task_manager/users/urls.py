from django.urls import path
from task_manager.users import views

urlpatterns = [
    path('', views.users),
    path('create/', views.UsersCreateView.as_view()),
    path('<pk>/update/', views.UsersUpdateView.as_view()),
    path('<pk>/delete/', views.UsersDeleteView.as_view()),
    path('login/', views.UserLoginView.as_view()),
    path('logout/', views.UserLogoutView.as_view()),
]
