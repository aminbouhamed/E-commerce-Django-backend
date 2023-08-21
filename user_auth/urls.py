from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UtilisateurSimpleViewSet
from django.views import static


router = DefaultRouter()
router.register(r'users', UtilisateurSimpleViewSet, basename='user')

urlpatterns = [
    path('api/', include(router.urls)),
   
]

