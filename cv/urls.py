from django.urls import path
from . import views

urlpatterns = [
    path('academicos/<int:perfil_id>/', views.productos_academicos, name='productos_academicos'),
    path('laborales/<int:perfil_id>/', views.productos_laborales, name='productos_laborales'),
    path('venta-garaje/<int:perfil_id>/', views.venta_garaje, name='venta_garaje'),
]
