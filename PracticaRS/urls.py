#encoding:utf-8

from django.urls import path
from django.contrib import admin
from main import views

urlpatterns = [
    path('', views.index),
    path('populate/', views.populateDB),
    path('admin/', admin.site.urls),
    path('animes_genero', views.animes_genero),
    path('mejores_animes/', views.mejores_animes),
    path('similar_anime', views.similarAnimes),
    path('recomendar', views.recomendar),
]