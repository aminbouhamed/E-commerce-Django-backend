from rest_framework import serializers
from .models import UtilisateurSimple, Livreur, Commercant, Consommateur

# Serializer for UtilisateurSimple model

class UtilisateurSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UtilisateurSimple
        fields = '__all__'


        
# Serializer for Livreur model, which is a type of UtilisateurSimple

class LivreurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livreur
        fields = '__all__'

# Serializer for Commercant model, which is a type of UtilisateurSimple

class CommercantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commercant
        fields = '__all__'

# Serializer for Consommateur model, which is a type of UtilisateurSimple

class ConsommateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consommateur
        fields = '__all__'
