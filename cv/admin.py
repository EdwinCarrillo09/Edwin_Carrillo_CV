from django.contrib import admin
from django.http import HttpResponse
from .models import Perfil, Experiencia, Habilidad, Certificado, Referencia

# Función simple que cierra la pestaña
def respuesta_cierre_pestana():
    return HttpResponse('<script type="text/javascript">window.close();</script>')

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    def response_change(self, request, obj):
        if "_continue" not in request.POST:
            return respuesta_cierre_pestana()
        return super().response_change(request, obj)

@admin.register(Experiencia)
class ExperienciaAdmin(admin.ModelAdmin):
    def response_change(self, request, obj):
        if "_continue" not in request.POST:
            return respuesta_cierre_pestana()
        return super().response_change(request, obj)

@admin.register(Habilidad)
class HabilidadAdmin(admin.ModelAdmin):
    def response_change(self, request, obj):
        if "_continue" not in request.POST:
            return respuesta_cierre_pestana()
        return super().response_change(request, obj)

@admin.register(Certificado)
class CertificadoAdmin(admin.ModelAdmin):
    def response_change(self, request, obj):
        if "_continue" not in request.POST:
            return respuesta_cierre_pestana()
        return super().response_change(request, obj)

@admin.register(Referencia)
class ReferenciaAdmin(admin.ModelAdmin):
    def response_change(self, request, obj):
        if "_continue" not in request.POST:
            return respuesta_cierre_pestana()
        return super().response_change(request, obj)