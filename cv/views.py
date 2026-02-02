from django.shortcuts import render, get_object_or_404
from .models import (
    Perfil,
    Experiencia,
    Habilidad,
    Referencia,
    Certificado,
    VentaGaraje,
    ProductoAcademico,
    ProductoLaboral
)


def home(request):
    perfil = Perfil.objects.order_by('-id').first()

    if not perfil:
        return render(request, 'cv/index.html', {'perfil': None})

    return ver_cv(request, perfil.id)


def ver_cv(request, perfil_id):
    perfil = get_object_or_404(Perfil, id=perfil_id)

    experiencias = Experiencia.objects.filter(
        perfil=perfil
    ).order_by('-inicio', '-id')

    habilidades = Habilidad.objects.filter(perfil=perfil)
    referencias = Referencia.objects.filter(perfil=perfil)

    cursos = Certificado.objects.filter(
        perfil=perfil,
        tipo='curso'
    ).order_by('-fecha_obtencion')

    reconocimientos = Certificado.objects.filter(
        perfil=perfil,
        tipo='reconocimiento'
    ).order_by('-fecha_obtencion')

    # ✅ CORRECTO SEGÚN MODELO
    productos_academicos = ProductoAcademico.objects.filter(
        perfil=perfil,
        activarparaqueseveaenfront=True
    )

    # ✅ CORRECTO SEGÚN MODELO
    productos_laborales = ProductoLaboral.objects.filter(
        perfil=perfil,
        activo=True
    )

    contexto = {
        'perfil': perfil,
        'experiencias': experiencias,
        'habilidades': habilidades,
        'referencias': referencias,
        'cursos': cursos,
        'reconocimientos': reconocimientos,
        'productos_academicos': productos_academicos,
        'productos_laborales': productos_laborales,
    }

    return render(request, 'cv/index.html', contexto)


def venta_garaje(request, perfil_id):
    ventas = VentaGaraje.objects.filter(
        perfil_id=perfil_id
    ).order_by('-fecha_publicacion')

    return render(request, 'cv/venta_garaje.html', {
        'ventas_garaje': ventas,
        'perfil_id': perfil_id
    })


def productos_academicos(request, perfil_id):
    perfil = get_object_or_404(Perfil, id=perfil_id)

    productos = ProductoAcademico.objects.filter(
        perfil=perfil,
        activarparaqueseveaenfront=True
    )

    return render(request, 'cv/productosacademicos.html', {
        'perfil': perfil,
        'productos': productos
    })


def productos_laborales(request, perfil_id):
    perfil = get_object_or_404(Perfil, id=perfil_id)

    productos = ProductoLaboral.objects.filter(
        perfil=perfil,
        activo=True
    )

    return render(request, 'cv/productos_laborales.html', {
        'perfil': perfil,
        'productos': productos
    })
