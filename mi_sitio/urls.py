from django.contrib import admin
from django.urls import include, path
from cv.views import home, ver_cv
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Página principal
    path('', home, name='home'),
    path('perfil/<int:perfil_id>/', ver_cv, name='ver_cv'),

    # App cv
    path('', include('cv.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
