from django.db import models
from datetime import date, datetime


# Create your models here.
class TodoList(models.Model):
    todo_title = models.CharField(name="Title", max_length=30)
    date = models.DateField(name="Date", default=date.today)


class Todo(models.Model):
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE, name="Todo_list")
    todo_detail = models.CharField(max_length=125, default="TODO OBJECT BLANK")


class Homework(models.Model):
    class_name = models.CharField(
        max_length=45, default="BLANK CLASS", blank=False, null=False
    )
    title = models.CharField(
        max_length=125, default="BLANK ASSIGNMENT TITLE", blank=False, null=False
    )
    detail = models.TextField(default="BLANK ASSIGNMENT DETAILS", null=False)
    due_date = models.DateTimeField(
        auto_now=False, auto_now_add=False, default=datetime.today
    )
