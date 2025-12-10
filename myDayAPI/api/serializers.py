from rest_framework import serializers
from .models import TodoList, Todo

class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = '__all__' 