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
    list_display = ('nombre', 'apellido', 'ver_perfil_boton')

    def ver_perfil_boton(self, obj):
        url = reverse('ver_cv', args=[obj.id])
        return format_html(
            '<a class="button" href="{}" target="_blank" '
            'style="background-color:#417690;color:white;padding:5px 12px;'
            'border-radius:4px;text-decoration:none;font-weight:bold;">Ver CV</a>',
            url
        )

    ver_perfil_boton.short_description = 'Acciones'

    def response_change(self, request, obj):
        if "_continue" not in request.POST:
            return respuesta_cierre_pestana()
        return super().response_change(request, obj)


@admin.register(Experiencia)
class ExperienciaAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'empresa', 'perfil')
    list_filter = ('perfil',)

    def response_change(self, request, obj):
        if "_continue" not in request.POST:
            return respuesta_cierre_pestana()
        return super().response_change(request, obj)


@admin.register(Habilidad)
class HabilidadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'perfil')
    list_filter = ('perfil', 'categoria')

    def response_change(self, request, obj):
        if "_continue" not in request.POST:
            return respuesta_cierre_pestana()
        return super().response_change(request, obj)


# =========================
#   ADMIN DE CURSOS
# =========================
class CursosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'institucion', 'fecha_obtencion', 'total_horas', 'perfil')
    list_filter = ('perfil', 'institucion')
    search_fields = ('titulo', 'institucion')
    exclude = ('tipo',)

    fieldsets = (
        ('Información del Curso', {
            'fields': ('perfil', 'titulo', 'institucion')
        }),
        ('Detalles Académicos', {
            'fields': ('fecha_obtencion', 'total_horas')
        }),
        ('Archivo', {
            'fields': ('archivo',)
        }),
    )

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


# =========================
#   ADMIN DE RECONOCIMIENTOS
# =========================
class ReconocimientosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'institucion', 'fecha_obtencion', 'perfil')
    list_filter = ('perfil', 'institucion')
    search_fields = ('titulo', 'institucion')
    exclude = ('tipo',)

    fieldsets = (
        ('Información del Reconocimiento', {
            'fields': ('perfil', 'titulo', 'institucion')
        }),
        ('Fecha', {
            'fields': ('fecha_obtencion',)
        }),
        ('Archivo', {
            'fields': ('archivo',)
        }),
    )

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


# =========================
#   PROXIES
# =========================
class CursoProxy(Certificado):
    class Meta:
        proxy = True
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"


class ReconocimientoProxy(Certificado):
    class Meta:
        proxy = True
        verbose_name = "Reconocimiento"
        verbose_name_plural = "Reconocimientos"


admin.site.register(CursoProxy, CursosAdmin)
admin.site.register(ReconocimientoProxy, ReconocimientosAdmin)


@admin.register(Referencia)
class ReferenciaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'perfil')
    list_filter = ('perfil',)

    def response_change(self, request, obj):
        if "_continue" not in request.POST:
            return respuesta_cierre_pestana()
        return super().response_change(request, obj)
from .models import VentaGaraje

@admin.register(VentaGaraje)
class VentaGarajeAdmin(admin.ModelAdmin):
    list_display = (
        'nombre_producto',
        'estado_producto',
        'valor_bien',
        'fecha_publicacion'
    )

    list_filter = ('estado_producto', 'fecha_publicacion')
    search_fields = ('nombre_producto', 'descripcion')
    ordering = ('-fecha_publicacion',)

