from django.db import models
from user_auth.models import UtilisateurSimple
from datetime import date , datetime
from user_auth.models import Commercant
# Create your models here.
class EventDetails(models.Model):
    EventId = models.AutoField(primary_key=True)
    EventName = models.CharField(max_length=500)
    EventDescription = models.CharField(max_length=500)
    DateEvent = models.DateField(auto_now_add=False,auto_now=False,blank=True,null=True)
    picture =  models.ImageField(upload_to='img', blank=True,null=True)   
    creator = models.ForeignKey(Commercant,null=True, on_delete=models.CASCADE)
    #vendor= models.OneToOneField(UtilisateurSimple, on_delete=models.CASCADE)
    pass