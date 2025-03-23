from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CardViewSet, TaskViewSet



router = DefaultRouter()
router.register(r'users', UserViewSet) 
router.register(r'cards', CardViewSet)  
router.register(r'tasks', TaskViewSet)  




urlpatterns = [
    path('', include(router.urls)),  
]
