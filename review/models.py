from django.db import models
from user_auth.models import Commercant , Consommateur
# Create your models here.
class Review(models.Model):
    ReviewId = models.AutoField(primary_key=True)
    ReviewRate = models.IntegerField(null=True)
    ReviewContent = models.TextField(null=True)
    DateReview = models.DateField(auto_now_add=False,auto_now=False,blank=True,null=True) 
    creator = models.ForeignKey(Consommateur,null=False, on_delete=models.CASCADE)
    ConcernedVendor = models.ForeignKey(Commercant,null=False,on_delete=models.CASCADE)
    ConcernedProduct=models.CharField(null=True,max_length=500)
    #vendor= models.OneToOneField(UtilisateurSimple, on_delete=models.CASCADE)
    pass