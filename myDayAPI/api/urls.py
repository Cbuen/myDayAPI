from django.urls import include, path
from rest_framework import routers

from . import views


urlpatterns = [
    path('todo-list/', views.TodoListView.as_view(), name='todo-lists'),
    path('todo-list/<int:pk>/', views.TodoListView.as_view(),name='todo-list'),
]