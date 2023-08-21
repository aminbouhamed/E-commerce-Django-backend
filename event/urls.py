from django.urls import path 
from .views import EventDetail 

eventviewsets = EventDetail.as_view({
    'get': 'list',
    'post': 'create',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

urlpatterns = [
    path('eventdetails',eventviewsets,name='event'),
    path('eventdetails/<int:pk>',eventviewsets)
    
]