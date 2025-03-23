from django.urls import path
from .views import UserViewSet, CardViewSet, TaskViewSet




user_list_create = UserViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
user_retrieve_update_destroy = UserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


card_list_create = CardViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
card_retrieve_update_destroy = CardViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


task_list_create = TaskViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
task_retrieve_update_destroy = TaskViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('users/', user_list_create, name='user-list-create'),
    path('user/<int:pk>/', user_retrieve_update_destroy, name='user-detail'),
    path('cards/', card_list_create, name='card-list-create'),
    path('card/<int:pk>/', card_retrieve_update_destroy, name='card-detail'),
    path('tasks/', task_list_create, name='task-list-create'),
    path('task/<int:pk>/', task_retrieve_update_destroy, name='task-detail'),
]
