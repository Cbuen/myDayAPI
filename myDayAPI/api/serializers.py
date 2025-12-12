from rest_framework import serializers
from .models import TodoList, Todo, Homework


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = "__all__"


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"


class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = "__all__"
