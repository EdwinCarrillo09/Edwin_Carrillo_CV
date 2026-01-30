from django.contrib import admin
from django.http import HttpResponse
from django.utils.html import format_html
from django.urls import reverse
from .models import Perfil, Experiencia, Habilidad, Certificado, Referencia

# Función simple que cierra la pestaña
def respuesta_cierre_pestana():
    return HttpResponse('<script type="text/javascript">window.close();</script>')

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    # Mostramos nombre y botón. Aquí el "dueño" es el perfil mismo.
    list_display = ('nombre', 'apellido', 'ver_perfil_boton')

    def ver_perfil_boton(self, obj):
        url = reverse('ver_cv', args=[obj.id])
        return format_html(
            '<a class="button" href="{}" target="_blank" style="background-color: #417690; color: white; padding: 5px 12px; border-radius: 4px; text-decoration: none; font-weight: bold;">Ver CV</a>',
            url
        )
    
    ver_perfil_boton.short_description = 'Acciones'

    def response_change(self, request, obj):
        if "_continue" not in request.POST:
            return respuesta_cierre_pestana()
        return super().response_change(request, obj)

@admin.register(Experiencia)
class ExperienciaAdmin(admin.ModelAdmin):
    # AÑADIDO: 'perfil' para ver de quién es la experiencia
    list_display = ('cargo', 'empresa', 'perfil') 
    list_filter = ('perfil',) # Filtro lateral para buscar por dueño

    def response_change(self, request, obj):
        if "_continue" not in request.POST:
            return respuesta_cierre_pestana()
        return super().response_change(request, obj)

@admin.register(Habilidad)
class HabilidadAdmin(admin.ModelAdmin):
    # AÑADIDO: 'perfil' y 'categoria'
    list_display = ('nombre', 'categoria', 'perfil')
    list_filter = ('perfil', 'categoria')

    def response_change(self, request, obj):
        if "_continue" not in request.POST:
            return respuesta_cierre_pestana()
        return super().response_change(request, obj)

class CursosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'institucion', 'perfil')
    list_filter = ('perfil',)
    exclude = ('tipo',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(tipo='curso')

    def save_model(self, request, obj, form, change):
        obj.tipo = 'curso'
        super().save_model(request, obj, form, change)

    def response_change(self, request, obj):
        if "_continue" not in request.POST:
            return respuesta_cierre_pestana()
        return super().response_change(request, obj)

class ReconocimientosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'institucion', 'perfil')
    list_filter = ('perfil',)
    exclude = ('tipo',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(tipo='reconocimiento')

    def save_model(self, request, obj, form, change):
        obj.tipo = 'reconocimiento'
        super().save_model(request, obj, form, change)

    def response_change(self, request, obj):
        if "_continue" not in request.POST:
            return respuesta_cierre_pestana()
        return super().response_change(request, obj)

# Proxy para Cursos
class CursoProxy(Certificado):
    class Meta:
        proxy = True
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

# Proxy para Reconocimientos
class ReconocimientoProxy(Certificado):
    class Meta:
        proxy = True
        verbose_name = "Reconocimiento"
        verbose_name_plural = "Reconocimientos"

admin.site.register(CursoProxy, CursosAdmin)
admin.site.register(ReconocimientoProxy, ReconocimientosAdmin)

@admin.register(Referencia)
class ReferenciaAdmin(admin.ModelAdmin):
    # AÑADIDO: 'perfil'
    list_display = ('nombre', 'perfil')
    list_filter = ('perfil',)

    def response_change(self, request, obj):
        if "_continue" not in request.POST:
            return respuesta_cierre_pestana()
        return super().response_change(request, obj)