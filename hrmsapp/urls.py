from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('demande_autorisation', views.demander_autorisation, name='demande_autorisation'),
    path('ajouter_collaborateur', views.ajouter_collaborateur, name='ajouter_collaborateur'),
]