from django.db import models

class Admin(models.Model):
    image_admin = models.ImageField(null=True, blank=True, upload_to='profile_images')
    nom_admin = models.CharField(max_length=32, null=True)
    prenom_admin = models.CharField(max_length=32, null=True)
    email_admin = models.EmailField(max_length=50)
    password_admin = models.CharField(max_length=50)
    date_inscription_admin = models.DateTimeField(auto_now_add=True)
    numero_telephone_admin = models.IntegerField(null=True)
    privilege = models.CharField(max_length=32, null=True)
    equipe = models.CharField(max_length=32, null=True)


    def __str__(self):
        return self.email_admin