from rest_framework import serializers
from .models import Admin

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['id', 'image_admin', 'nom_admin', 'prenom_admin', 'email_admin', 'password_admin', 'date_inscription_admin', 'numero_telephone_admin', 'privilege', 'equipe']
