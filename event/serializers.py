from rest_framework import serializers
from event.models import EventDetails 



class EventSerializer(serializers.ModelSerializer): 
   
    class Meta: 
        model= EventDetails 
        fields = '__all__'

