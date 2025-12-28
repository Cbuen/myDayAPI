from rest_framework import serializers
from .models import TodoList, Todo, Homework
from django.contrib.auth.models import User


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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
       model = User
       fields = "__all__" 

    def create(self, validated_data):
        user = User(
            username=validated_data["username"],
            email=validated_data.get("email","")
        )
        user.set_password(validated_data["password"])
        user.save()
        return user