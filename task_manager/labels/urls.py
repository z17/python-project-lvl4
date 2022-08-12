from django.urls import path
from task_manager.labels import views

urlpatterns = [
    path('', views.LabelListView.as_view()),
    path('create/', views.LabelCreateView.as_view()),
    path('<pk>/update/', views.LabelUpdateView.as_view()),
    path('<pk>/delete/', views.LabelDeleteView.as_view()),
]
