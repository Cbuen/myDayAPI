from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from .serializers import TodoListSerializer
from .models import TodoList

"""
API View can only implicitly call get, delete, etc
to define custom requests, we must define helper function
"""
class TodoListView(APIView):
    # helper function
    def get_object(self,pk):
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