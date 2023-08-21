# urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Liste des URL pour l'application principale
urlpatterns = [
    # URL pour l'interface d'administration Django
    path('admin/', admin.site.urls),
    
    # URL pour l'application "user_auth"
    # Inclut les URL définies dans le fichier "urls.py" de l'application "user_auth"
    path('', include('user_auth.urls')),
    
    # URL pour l'application "admin_auth"
    # Inclut les URL définies dans le fichier "urls.py" de l'application "admin_auth"
    path('apii/', include('admin_auth.urls')),
    # url pour l'application eventdetails 
    path ('',include('event.urls')),
    path('',include('notification.urls')),
    path('',include('review.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Configuration des URL pour les fichiers médias

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # Configuration des URL pour les fichiers statiques
