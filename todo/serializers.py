from rest_framework import serializers
from todo.models import ToDo

class ToDOSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = 'id', 'text', 'done'