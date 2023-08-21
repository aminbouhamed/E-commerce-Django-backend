from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import  JSONParser
from django.http.response import JsonResponse 
from django.views.generic import DetailView, ListView
from rest_framework import status
from .models import Review
from user_auth.models import Commercant , Consommateur
from review.serializers import ReviewSerializer 
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
# Create your views here.

# Create your views here.
class ReviewDetail(ModelViewSet): 
    queryset = Review.objects.all()
    serializer_class=ReviewSerializer
    @classmethod
    def get_extra_actions(cls):
        return [] 
    def create(self, request, *args, **kwargs):
        return self.postreview(request)
    @action(detail=False, methods=['GET'])    
    def getreview(self,request):
        reviewdata = Review.objects.all()
        reviewserializer = ReviewSerializer(reviewdata,many=True)
        return Response(reviewserializer.data,status=status.HTTP_200_OK)
    @action(detail=False, methods=['POST'])
    def postreview(self, request):
        reviewserializer = ReviewSerializer(data=request.data)
        if reviewserializer.is_valid():
            event = reviewserializer.save()  


 


            '''if vendor:
                # Create Reviews for clients
                clients = Consommateur.objects.all()
                reviewcontent = f"A new event '{event.EventName}' has been created."
                print (reviewcontent)
                for client in clients:
                    Review = Review.objects.create(
                        user=client,
                        event=event,
                        content=reviewcontent,
                    )
                    Review.save()
                    print(client)
            '''
                # Create Reviews for vendors (except the event creator)
            '''other_vendors = Commercant.objects.all()
                for other_vendor in other_vendors:
                    Review = Review.objects.create(
                        user=other_vendor,
                        event=event,
                        content=reviewcontent,
                    )
                    Review.save()'''

            return Response(reviewserializer.data, status=status.HTTP_201_CREATED)

        return Response(reviewserializer.data, status=status.HTTP_400_BAD_REQUEST)
    @action(detail=False, methods=['DELETE'])
    def deleteReview(self,request,pk): 
        try:
            obj=Review.objects.get(EventId=pk)
        except Review.DoesNotExist:
            msg = {'msg':'Event Not Found'}
            return Response(msg , status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response({'msg':'deleted'},status=status.HTTP_204_NO_CONTENT)
