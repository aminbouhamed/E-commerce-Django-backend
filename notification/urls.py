from django.urls import path 
from .views import NotificationDetail

notificationviewsets = NotificationDetail.as_view({
    'get': 'list',
    'post': 'create',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

urlpatterns = [
    path('notificationdetails',notificationviewsets,name='notification'),
    path('notificationdetails/<int:pk>',notificationviewsets)
    
]