from rest_framework import viewsets
from .models import User, Card, Task
from .serializers import UserSerializer, CardSerializer, TaskSerializer




class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all() 
    serializer_class = UserSerializer  


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all() 
    serializer_class = CardSerializer  
    

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()  
    serializer_class = TaskSerializer
