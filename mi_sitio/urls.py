from django.contrib import admin
from django.urls import path
from cv.views import (
    home,
    ver_cv,
    venta_garaje,
    productos_academicos,
    productos_laborales   # 👈 agregado
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home
    path('', home, name='home'),

    # CV
    path('perfil/<int:perfil_id>/', ver_cv, name='ver_cv'),

    # Venta Garaje
    path('venta-garaje/<int:perfil_id>/', venta_garaje, name='venta_garaje'),

    # Productos Académicos
    path(
        'productos-academicos/<int:perfil_id>/',
        productos_academicos,
        name='productos_academicos'
    ),

    # Productos Laborales ✅ NUEVO
    path(
        'productos-laborales/<int:perfil_id>/',
        productos_laborales,
        name='productos_laborales'
    ),

    # (la dejo tal cual la tienes, aunque esté repetida)
    path('perfil/<int:perfil_id>/', ver_cv, name='ver_cv'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
