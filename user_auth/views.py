from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.exceptions import ValidationError
from .models import UtilisateurSimple, Livreur, Commercant, Consommateur
from .serializers import (
    UtilisateurSimpleSerializer,
    LivreurSerializer,
    CommercantSerializer,
    ConsommateurSerializer,
)

class UtilisateurSimpleViewSet(ModelViewSet):
    queryset = UtilisateurSimple.objects.all()
    serializer_class = UtilisateurSimpleSerializer

    @classmethod
    def get_extra_actions(cls):
        return [] 

    def create(self, request, *args, **kwargs):
        return self.create_utilisateur(request)

  #Create user 

    @action(detail=False, methods=['POST'])
    def create_utilisateur(self, request):
        data = request.data.copy()
        # Ajouter l'identifiant Firebase à la requête.
        data['firebase_uid'] = request.firebase_uid 
        print('Received data:', data)

        # Supposons que vous ayez un moyen d'identifier le rôle de l'utilisateur (Consommateur, Livreur, Commercant)
        role = data.get('role', 'Consommateur')
        if role == 'Consommateur':
            serializer = ConsommateurSerializer(data=data)
        elif role == 'Livreur':
            serializer = LivreurSerializer(data=data)
        elif role == 'Commercant':
            serializer = CommercantSerializer(data=data)
        else:
            raise ValidationError({"role": "Invalid role specified."})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    #Update user 

    @action(detail=True, methods=['PUT'])
    def update_utilisateur(self, request, pk=None):
        utilisateur = self.get_object()
        data = request.data.copy()
        firebase_uid = data.get('firebase_uid')  # Récupérer l'identifiant Firebase de la requête

        # Vérifier si l'identifiant Firebase est fourni dans les données de la requête
        if not firebase_uid:
            raise ValidationError({"firebase_uid": "firebase_uid field is required."})

        # Vérifier si l'identifiant Firebase fourni existe déjà dans la base de données 
        if UtilisateurSimple.objects.filter(firebase_uid=firebase_uid).exclude(pk=utilisateur.pk).exists():
            raise ValidationError({"firebase_uid": "This firebase_uid is already registered."})

       
        role = data.get('role', utilisateur.role)
        if role == 'Consommateur':
            serializer = ConsommateurSerializer(utilisateur, data=data)
        elif role == 'Livreur':
            serializer = LivreurSerializer(utilisateur, data=data)
        elif role == 'Commercant':
            serializer = CommercantSerializer(utilisateur, data=data)
        else:
            raise ValidationError({"role": "Invalid role specified."})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# Retrieve user

    @action(detail=True, methods=['GET'])
    def retrieve_utilisateur(self, request, pk=None):
        utilisateur = self.get_object()
       # Déterminer le rôle de l'utilisateur (Consommateur, Livreur, Commercant) pour sélectionner le serializer approprié
        role = utilisateur.role
        if role == 'Consommateur':
            serializer = ConsommateurSerializer(utilisateur)
        elif role == 'Livreur':
            serializer = LivreurSerializer(utilisateur)
        elif role == 'Commercant':
            serializer = CommercantSerializer(utilisateur)
        else:
             # Si un rôle invalide est spécifié, lever une erreur 
            raise ValidationError({"role": "Invalid role specified."})
            # Sérialiser les données de l'utilisateur en utilisant le sérialiseur sélectionné
        serialized_data = serializer.data

            # Préparer les données de la réponse avec des métadonnées supplémentaires (statut et message)

        data = serialized_data
        status = "success"
        message = "Utilisateur retrieved successfully"

        response_data = {
            "data": data,
            "status": status,
            "message": message
        }

        response_data.update(serialized_data) 

        return Response(response_data)

    #Delete user
    @action(detail=True, methods=['DELETE'])
    def destroy(self, request, *args, **kwargs):
        # Récupérer l'instance de l'utilisateur à supprimer
        instance = self.get_object()
         # Appeler la méthode perform_destroy pour effectuer la suppression
        self.perform_destroy(instance)
        return Response(status=204)
