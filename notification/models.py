from django.db import models
from user_auth.models import UtilisateurSimple
from event.models import EventDetails 
# Create your models here.
class Notification(models.Model):
    event = models.ForeignKey(EventDetails, on_delete=models.CASCADE,null=True)  
    creator_info=models.TextField(null=True)
    content= models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
     

    def __str__(self):
        return f"Notification to {self.user} about {self.event}"