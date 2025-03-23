from rest_framework import serializers
from .models import User, Card, Task




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' 


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'  


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'  
