from firebase_admin import auth
from django.http import JsonResponse

def firebase_auth_middleware(get_response):
    # Liste des URL exclues qui ne nécessitent pas d'authentification Firebase
    excluded_urls = [
             
        '/apii/login',            
        '/apii/admin',
        '/eventdetails',
        '/notificationdetails',
        '/reviewdetails',
        '/favoris'    

        # Ajoutez d'autres URL que vous souhaitez exclure de l'authentification ici
    ]

    def middleware(request):
        path_info = request.path_info

        # Vérifie si l'URL actuelle est dans la liste des URL exclues
        for url in excluded_urls:
            if path_info.startswith(url):
                return get_response(request)

        # Récupère l'en-tête d'autorisation (Authorization header)
        auth_header = request.META.get('HTTP_AUTHORIZATION')

        if auth_header:
            try:
                # Extrait le jeton d'identification (ID token) du header d'autorisation
                _, id_token = auth_header.split(' ')
                # Vérifie le jeton d'identification auprès de Firebase
                decoded_token = auth.verify_id_token(id_token)
                uid = decoded_token['uid']

                # Ajoute l'identifiant Firebase de l'utilisateur à la requête
                request.firebase_uid = uid

                return get_response(request)

            except auth.InvalidIdTokenError:
                # Le jeton d'identification est invalide, renvoie une réponse d'erreur
                return JsonResponse({'error': 'Invalid ID token'}, status=401)

        # Si l'en-tête d'autorisation est manquant, renvoie une réponse d'erreur
        return JsonResponse({'error': 'Authorization header missing'}, status=401)

    return middleware
