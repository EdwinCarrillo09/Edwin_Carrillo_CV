from django.shortcuts import render, get_object_or_404
from .models import (
    Perfil,
    Experiencia,
    Habilidad,
    Referencia,
    Certificado,
    ProductoAcademico,
    ProductoLaboral,
    VentaGaraje
)


def home(request):
    # Traer el último perfil creado
    perfil = Perfil.objects.order_by('-id').first()

    if not perfil:
        return render(request, 'cv/index.html', {'perfil': None})

    return ver_cv(request, perfil.id)


def ver_cv(request, perfil_id):
    # Traer el perfil correcto por ID
    perfil = get_object_or_404(Perfil, id=perfil_id)

    experiencias = (
        Experiencia.objects
        .filter(perfil=perfil)
        .order_by('-inicio', '-id')
    )

    habilidades = Habilidad.objects.filter(perfil=perfil)
    referencias = Referencia.objects.filter(perfil=perfil)

    # Cursos
    cursos = (
        Certificado.objects
        .filter(perfil=perfil, tipo='curso')
        .order_by('-fecha_obtencion')
    )

    # Reconocimientos
    reconocimientos = (
        Certificado.objects
        .filter(perfil=perfil, tipo='reconocimiento')
        .order_by('-fecha_obtencion')
    )

    # 🔹 PRODUCTOS (ESTO ES LO QUE FALTABA)
    productos_academicos = ProductoAcademico.objects.filter(
        perfil=perfil,
        activarparaqueseveaenfront=True
    )

    productos_laborales = ProductoLaboral.objects.filter(
        perfil=perfil,
        activarparaqueseveaenfront=True
    )

    ventas_garaje = VentaGaraje.objects.filter(
        perfil=perfil,
        activarparaqueseveaenfront=True
    )

    contexto = {
        'perfil': perfil,
        'experiencias': experiencias,
        'habilidades': habilidades,
        'referencias': referencias,
        'cursos': cursos,
        'reconocimientos': reconocimientos,

        # 👇 YA VIAJAN AL FRONT
        'productos_academicos': productos_academicos,
        'productos_laborales': productos_laborales,
        'ventas_garaje': ventas_garaje,
    }

    return render(request, 'cv/index.html', contexto)


# 🔸 ESTAS VISTAS SE DEJAN (NO MOLESTAN)
def productos_academicos(request, perfil_id):
    productos = ProductoAcademico.objects.filter(
        perfil_id=perfil_id,
        activarparaqueseveaenfront=True
    )
    return render(request, 'cv/productos_academicos.html', {
        'productos': productos
    })


def productos_laborales(request, perfil_id):
    productos = ProductoLaboral.objects.filter(
        perfil_id=perfil_id,
        activarparaqueseveaenfront=True
    )
    return render(request, 'cv/productos_laborales.html', {
        'productos': productos
    })


def venta_garaje(request, perfil_id):
    productos = VentaGaraje.objects.filter(
        perfil_id=perfil_id,
        activarparaqueseveaenfront=True
    )
    return render(request, 'cv/venta_garaje.html', {
        'productos': productos
    })
