from django.urls import path
from task_manager.tasks import views

app_name = 'tasks'

urlpatterns = [

    path('', views.TaskListView.as_view(), name='index'),
    path('create/', views.TaskCreateView.as_view(), name='create'),
    path('<pk>/update/', views.TaskUpdateView.as_view(), name='update'),
    path('<pk>/delete/', views.TaskDeleteView.as_view(), name='delete'),
    path('<pk>/', views.TaskView.as_view(), name='task'),
]
