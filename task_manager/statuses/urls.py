from django.urls import path
from task_manager.statuses import views

app_name = 'statuses'

urlpatterns = [
    path('', views.StatusListView.as_view(), name='index'),
    path('create/', views.StatusCreateView.as_view(), name='create'),
    path('<pk>/update/', views.StatusUpdateView.as_view(), name='update'),
    path('<pk>/delete/', views.StatusDeleteView.as_view(), name='delete'),
]
