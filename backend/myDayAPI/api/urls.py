from django.urls import include, path
from rest_framework import routers

from . import views


urlpatterns = [
    path("todo-list/", views.TodoListView.as_view(), name="todo-lists"),
    path("todo-list/<int:pk>/", views.TodoListView.as_view(), name="todo-list"),
    path("todo/", views.TodoView.as_view(), name="todos"),
    path("todo/<int:pk>/", views.TodoView.as_view(), name="todo"),
    path("homework/", views.HomeworkView.as_view(), name="homeworks"),
    path("homework/<int:pk>/", views.HomeworkView.as_view(), name="homework"),
    path("users/", views.UserManagementView.as_view(), name="users"),
    path("users/<int:pk>/", views.UserManagementView.as_view(), name="user"),
    path("users/signup", views.UserManagementView.as_view(), name="users-signup"),
    path("login/", views.LoginUserView.as_view(), name="login-user"),
]
