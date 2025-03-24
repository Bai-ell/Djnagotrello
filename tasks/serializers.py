from rest_framework import serializers
from .models import User, Card, Task




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'




class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'




class CardSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)
    
    class Meta:
        model = Card
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True} 
        }



class TaskUpdateSerializer(serializers.Serializer):
    task_id = serializers.IntegerField()
    done = serializers.BooleanField()


class TaskDeleteSerializer(serializers.Serializer):
    task_id = serializers.IntegerField()