from django.urls import path
from .views import (
    TaskListView,
    TaskToggleDoneView,
    TaskUpdateView,
    TaskDeleteView,
)

app_name = 'tasks'

urlpatterns = [
    path('', TaskListView.as_view(), name='list'),
    path('<int:pk>/toggle/', TaskToggleDoneView.as_view(), name='toggle'),
    path('<int:pk>/edit/', TaskUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='delete'),
]