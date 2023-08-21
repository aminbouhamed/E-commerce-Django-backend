from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import  JSONParser
from django.http.response import JsonResponse 
from django.views.generic import DetailView, ListView
from rest_framework import status
from event.models import EventDetails 
from .models import Notification
from user_auth.models import Commercant , Consommateur
from notification.serializers import NotificationSerializer 
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class NotificationDetail(ModelViewSet): 
    queryset = Notification.objects.all()
    serializer_class=NotificationSerializer
    @classmethod
    def get_extra_actions(cls):
        return [] 
    def create(self, request, *args, **kwargs):
        return self.postnotification(request)
    @action(detail=False, methods=['GET'])    
    def getnotification(self,request):
        notification_data = Notification.objects.all()
        notification_serializer = NotificationSerializer(notification_data,many=True)
        return Response(notification_serializer.data,status=status.HTTP_200_OK)
    @action(detail=False, methods=['POST'])
    def postnotification(self, request):
        notification_serializer = NotificationSerializer(data=request.data)
        if notification_serializer.is_valid():
            event = notification_serializer.save()  


 


            '''if vendor:
                # Create notifications for clients
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

            return Response(notification_serializer.data, status=status.HTTP_201_CREATED)

        return Response(notification_serializer.data, status=status.HTTP_400_BAD_REQUEST)
    @action(detail=False, methods=['DELETE'])
    def deletenotification(self,request,pk): 
        try:
            obj=Notifications.objects.get(EventId=pk)
        except Notifications.DoesNotExist:
            msg = {'msg':'Event Not Found'}
            return Response(msg , status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response({'msg':'deleted'},status=status.HTTP_204_NO_CONTENT)
