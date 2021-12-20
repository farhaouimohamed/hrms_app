from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('login',views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('addAdminUser', views.addAdminUser, name='addAdminUser'),
    path('admin_iga/profile', views.profil_admin, name='profil_admin'),
    path('responsable/profile', views.profil_responsable, name='profil_responsable'),
    path('developpeur/demande_autorisation', views.demander_autorisation, name='demande_autorisation'),
    path('developpeur/liste_autorisations_validees', views.list_autorisations_validees, name='liste_autorisations_validees'),
    path('developpeur/liste_autorisations_non_validees', views.list_autorisations_non_validees, name='liste_autorisations_non_validees'),
    path('developpeur/liste_autorisations_en_cours', views.list_autorisations_en_cours, name='liste_autorisations_en_cours'),
    path('detail_autorisation/<str:pk>/', views.detail_autorisation, name='detail_autorisation'),
    path('admin_iga/ajouter_collaborateur', views.ajouter_collaborateur, name='ajouter_collaborateur'),
    path('admin_iga/liste_collaborateurs', views.list_collaborateur_admin, name='ajouter_collaborateur_admin'),
    path('responsable/liste_collaborateur', views.list_collaborateur_resp, name='liste_collaborateur_resp'),
    path('responsable/liste_autorisations_validees', views.list_autorisations_validees_resp, name='liste_autorisations_validees_resp'),
    path('responsable/liste_autorisations_non_validees', views.list_autorisations_non_validees_resp, name='liste_autorisations_non_validees_resp'),
    path('responsable/liste_autorisations_en_cours', views.list_autorisations_en_cours_resp, name='liste_autorisations_en_cours_resp'),
    path('valider_autorisation/<str:pk>/', views.valider_autorisation, name='valider_autorisation'),
]