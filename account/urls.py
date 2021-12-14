from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.pageAcceuil, name='acceuil'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]