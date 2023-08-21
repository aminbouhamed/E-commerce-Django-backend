from django.db import models

# Modèle pour représenter un UtilisateurSimple

class UtilisateurSimple(models.Model):
    firebase_uid = models.CharField(primary_key=True, max_length=150)
    image = models.ImageField(null=True, blank=True, upload_to='profile_images')
    nom = models.CharField(max_length=32, null=True)
    prenom = models.CharField(max_length=32, null=True)
    email = models.EmailField(max_length=50, null=True)
    date_inscription = models.DateTimeField(auto_now_add=True)
    adresse = models.CharField(max_length=100, null=True)
    role = models.CharField(max_length=30, default='Consommateur')
    etat = models.CharField(max_length=30, null=True)
    numero_telephone = models.IntegerField(null=True)
    password = models.CharField(max_length=128, null=True)
    confirm_password = models.CharField(max_length=128, null=True)

    def __str__(self):
        return self.email
# Modèle pour représenter un Livreur, qui est un type d'UtilisateurSimple
class Livreur(UtilisateurSimple):
    vehicule = models.CharField(max_length=100, null=True)
    horaire_de_travail = models.CharField(max_length=100, null=True)
    zone_de_travail = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"Livreur - {self.email}"



# Modèle pour représenter un Commercant, qui est un type d'UtilisateurSimple
class Commercant(UtilisateurSimple):
    description = models.TextField(null=True)

    def __str__(self):
        return f"Commercant - {self.email}"


# Modèle pour représenter un Consommateur, qui est un type d'UtilisateurSimple

class Consommateur(UtilisateurSimple):
    # Add attributes specific to the Consommateur model here
    pass
