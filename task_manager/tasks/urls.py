from django.urls import path
from task_manager.tasks import views

urlpatterns = [

    path('', views.TaskListView.as_view()),
    path('create/', views.TaskCreateView.as_view()),
    path('<pk>/update/', views.TaskUpdateView.as_view()),
    path('<pk>/delete/', views.TaskDeleteView.as_view()),
    path('<pk>/', views.TaskView.as_view(), name='task'),
]
