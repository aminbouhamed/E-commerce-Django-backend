from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import  JSONParser
from django.http.response import JsonResponse 
from django.views.generic import DetailView, ListView
from rest_framework import status
from .models import EventDetails 
from user_auth.models import Commercant , Consommateur
from event.serializers import EventSerializer 
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet



# Create your views here.
'''def EventApi(request,id=0):
    if request.method == 'GET' : 
        Event = EventDetails.objects.all()
        Event_serializer =EventSerializer(Event,many=True) 
        return JsonResponse(Event_serializer.data,safe=False)
    elif request.method == 'POST' : 
        Event_Data = JSONParser().parse(request)
        Event_serializer = EventSerializer(data=Event_Data)
        if Event_serializer.is_valid() : 
            Event_serializer.save()
            return JsonResponse("added successfully", safe=False)
        return JsonResponse("failed to add", safe=False)
    
    elif request.method == 'DELETE': 
        Event=EventDetails.objects.get(EventId=id)
        Event.delete()
        return JsonResponse ("deleted successfully", safe=False)'''
class EventDetail(ModelViewSet): 
    queryset = EventDetails.objects.all()
    serializer_class=EventSerializer
    @classmethod
    def get_extra_actions(cls):
        return [] 

    def create(self, request, *args, **kwargs):
        return self.postevent(request)
    @action(detail=False, methods=['GET'])    
    def getevent(self,request):
        event_data = EventDetails.objects.all()
        Event_serializer = EventSerializer(event_data,many=True)
        return Response(Event_serializer.data,status=status.HTTP_200_OK)
    @action(detail=False, methods=['POST'])
    def postevent(self, request):
        Event_serializer = EventSerializer(data=request.data)
        if Event_serializer.is_valid():
            event = Event_serializer.save()  

            # Retrieve the vendor who created the event based on email4
            print("Request data:", request.data)
            creator_id = request.data.get('creator')  # Replace with actual field name
            print(Commercant.objects)
            vendor = Commercant.objects.filter(utilisateursimple_ptr_id=creator_id).first()
            print (creator_id)
            print(vendor)
 


            if vendor:
                '''# Create notifications for clients
                clients = Consommateur.objects.all()
                notification_content = f"A new event '{event.EventName}' has been created."
                print (notification_content)
                for client in clients:
                    notification = Notification.objects.create(
                        user=client,
                        event=event,
                        content=notification_content,
                    )
                    notification.save()
                    print(client)
                '''
                # Create notifications for vendors (except the event creator)
                '''other_vendors = Commercant.objects.all()
                for other_vendor in other_vendors:
                    notification = Notification.objects.create(
                        user=other_vendor,
                        event=event,
                        content=notification_content,
                    )
                    notification.save()'''

                return Response(Event_serializer.data, status=status.HTTP_201_CREATED)

        return Response(Event_serializer.data, status=status.HTTP_400_BAD_REQUEST)
    @action(detail=False, methods=['DELETE'])
    def deleteevent(self,request,pk): 
        try:
            obj=EventDetails.objects.get(EventId=pk)
        except EventDetails.DoesNotExist:
            msg = {'msg':'Event Not Found'}
            return Response(msg , status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response({'msg':'deleted'},status=status.HTTP_204_NO_CONTENT)


