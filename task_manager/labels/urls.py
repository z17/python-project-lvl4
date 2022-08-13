from django.urls import path
from task_manager.labels import views

app_name = 'labels'

urlpatterns = [
    path('', views.LabelListView.as_view(), name='index'),
    path('create/', views.LabelCreateView.as_view(), name='create'),
    path('<pk>/update/', views.LabelUpdateView.as_view(), name='update'),
    path('<pk>/delete/', views.LabelDeleteView.as_view(), name='delete'),
]
