from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .serializers import (
    TodoListSerializer,
    TodoSerializer,
    HomeworkSerializer,
    UserSerializer,
)
from .models import TodoList, Todo, Homework

"""
API View can only implicitly call get, delete, etc
to define custom requests, we must define helper function
"""


class TodoListView(APIView):
    """
    Docstring for TodoListView
    Todo list view for CRUD On todo lists
    """
    def get_object(self, pk):
        try:
            return TodoList.objects.get(pk=pk)
        except TodoList.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        todolists = TodoList.objects.all()
        serializer = TodoListSerializer(todolists, many=True)
        if pk:
            todolists = self.get_object(pk)
            serializer = TodoListSerializer(todolists)
            return Response(serializer.data)

        return Response(serializer.data)

    def delete(self, request, pk=None, format=None):
        if pk:
            self.get_object(pk)
            todolist = TodoList.objects.get(pk=pk)
            todolist.delete()
        else:
            todolists = TodoList.objects.all()
            todolists.delete()

        return Response(status=status.HTTP_202_ACCEPTED)

    def post(self, request):
        serializer = TodoListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoView(APIView):
    """
    Docstring for TodoView
    View for individual todo object CRUD operations 
    """
    def get_object(self, pk):
        try:
            return Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            todo = self.get_object(pk)
            serializer = TodoSerializer(todo)
            return Response(serializer.data)

        todo = Todo.objects.all()
        serializer = TodoSerializer(todo, many=True)
        if len(serializer.data) == 0:
            return Response(status.HTTP_204_NO_CONTENT)
        return Response(serializer.data)

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        todo = self.get_object(pk)
        todo.delete()
        return Response(status=status.HTTP_200_OK)


class HomeworkView(APIView):
    """
    Docstring for HomeworkView
    View for later implementation for "student" API section Homework objects
    """

    def get_object(self, pk):
        try:
            homework = Homework.objects.get(pk=pk)
            return homework
        except Homework.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            homework = self.get_object(pk=pk)
            seralizer = HomeworkSerializer(homework)
            return Response(seralizer.data)

        homeworks = Homework.objects.all()
        seralizer = HomeworkSerializer(homeworks)
        return Response(seralizer.data)

    def post(self, request):

        if not request.data:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = HomeworkSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserManagementView(APIView):
    """
    Docstring for UserManagementView
    Usermanagment view handles all things realted to user CRUD operations
    Signup request json structure {"username": "username", "password": "password"}
    TODO:
    Set permissions for view for security
    Create seperate loginclassview for users
    Add put functions for user object update

    """

    # do not expose this in production
    # for debug purposes to test API and mutiple users
    def get(self, request, pk=None):
        if pk:
            try:
                user = User.objects.get(pk=pk)
                serializer = UserSerializer(user)
                return Response(data=serializer.data)
            except User.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data={"message": f"User created {request.data["username"]}"})
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": "no form data"})


class LoginUserView(APIView):
    """
    LoginUserView handles login user auth activites
    Standard login request:
    {"username":  "username", "password": "password"}
    """

    def get(self, request):
        if request.user.is_authenticated:
            return Response(data={"message": f"{request.user} is logged in"})
        else:
            return Response(data={"message": "please login!"})

    def post(self, request):
        # login function
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        print(username, password)
        user = authenticate(username=username, password=password)
        if request.user.is_authenticated:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"message": f"{request.user} is already logged in!"},
            )
        if user is not None:
            login(request, user)
            return Response(
                status=status.HTTP_202_ACCEPTED,
                data={"message": f"User {request.user} is now logged in"},
            )

        return Response(status=status.HTTP_404_NOT_FOUND)
    

class LogoutUserView(APIView):
    """
    Docstring for LogoutUserView
    Handles logout user for a logged in / authenticated user
    """
    def get(self, request):
        if request.user.is_authenticated:
            return Response(data={"message": f"{request.user} is logged in"})
        else:
            return Response(data={"message": "please login!"})

    def post(self, request):
        if request.user.is_authenticated:
            logged_out_user = request.user
            logout(request)
            return Response(status=status.HTTP_200_OK, data={"message": f"{logged_out_user} has been logged out!"})
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED, data={"message": "must be logged in!"})

