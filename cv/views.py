from django.shortcuts import render, get_object_or_404
from .models import Perfil, Experiencia, Habilidad, Referencia, Certificado, VentaGaraje


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

    # Separar Cursos y Reconocimientos
    cursos = (
        Certificado.objects
        .filter(perfil=perfil, tipo='curso')
        .order_by('-fecha_obtencion')  
    )

    reconocimientos = (
        Certificado.objects
        .filter(perfil=perfil, tipo='reconocimiento')
        .order_by('-fecha_obtencion')  
    )

    contexto = {
        'perfil': perfil,
        'experiencias': experiencias,
        'habilidades': habilidades,
        'referencias': referencias,
        'cursos': cursos,
        'reconocimientos': reconocimientos,
    }

    return render(request, 'cv/index.html', contexto)

def venta_garaje(request, perfil_id):
    perfil = get_object_or_404(Perfil, id=perfil_id)
    ventas_garaje = VentaGaraje.objects.filter(
        perfil=perfil,
        activo_front=True
    )

    return render(request, 'cv/venta_garaje.html', {
        'perfil': perfil,
        'ventas_garaje': ventas_garaje
    })
