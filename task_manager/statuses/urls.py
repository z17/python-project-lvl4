from django.urls import path
from task_manager.statuses import views

urlpatterns = [
    path('', views.StatusListView.as_view()),
    path('create/', views.StatusCreateView.as_view()),
    path('<pk>/update/', views.StatusUpdateView.as_view()),
    path('<pk>/delete/', views.StatusDeleteView.as_view()),
]
