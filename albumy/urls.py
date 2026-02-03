from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_albumow, name='lista_albumow'),
    path('album/<int:id>/', views.szczegoly_albumu, name='szczegoly_albumu'),
    path('album/<int:id>/wypozycz/', views.wypozycz_album, name='wypozycz'),
    path('moje-wypozyczenia/', views.moje_wypozyczenia, name='moje_wypozyczenia'),
    path('zwroc/<int:id>/', views.zwroc_album, name='zwroc'),
    path('rejestracja/', views.rejestracja, name='rejestracja'),
]