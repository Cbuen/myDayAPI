from django.db import models
from datetime import date

# Create your models here.
class TodoList(models.Model):
    todo_title = models.CharField(name="Title", max_length=30)
    date = models.DateField(name="Date", default=date.today)

class Todo(models.Model):
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)