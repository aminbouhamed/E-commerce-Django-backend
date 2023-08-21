from django.urls import path 
from .views import ReviewDetail

reviewviewsets = ReviewDetail.as_view({
    'get': 'list',
    'post': 'create',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

urlpatterns = [
    path('reviewdetails',reviewviewsets,name='review'),
    path('reviewdetails/<int:pk>',reviewviewsets)
    
]