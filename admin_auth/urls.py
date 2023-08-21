
from django.urls import path
from .views import  AdminLoginView ,AdminView,LogoutView

urlpatterns = [
    path('login', AdminLoginView.as_view()),
    path('admin', AdminView.as_view()),
    path('logout', LogoutView.as_view()),
    

]
