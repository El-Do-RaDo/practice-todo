from  rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from todo.serializers import ToDOSerializer
from todo.models import ToDo

class ToDoListView(APIView):
    def get(self, request):
        todos = ToDo.objects.all()
        serializer = ToDOSerializer(todos, many=True)
        return Response(serializer.data)

    def put(self, request):
        serializer = ToDOSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ToDoDetailView(APIView):
    def get(self, request, pk):
        todo = get_object_or_404(ToDo, pk=pk)
        serializer = ToDOSerializer(todo)
        return Response(serializer.data)
    
    def delete(self, request, pk):
        todo = get_object_or_404(ToDo, pk=pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

