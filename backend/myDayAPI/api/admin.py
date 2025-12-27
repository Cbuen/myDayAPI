from django.contrib import admin
from .models import TodoList, Todo, Homework

# Register your models here.
admin.site.register((TodoList, Todo, Homework))
