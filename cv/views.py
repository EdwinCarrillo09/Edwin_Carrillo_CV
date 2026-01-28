from django.shortcuts import render, get_object_or_404
from .models import Perfil, Experiencia, Habilidad, Referencia, Certificado

def ver_cv(request, perfil_id):
    # Traer el perfil correcto por ID
    perfil = get_object_or_404(Perfil, id=perfil_id)

    experiencias = Experiencia.objects.filter(perfil=perfil).order_by('-inicio')
    habilidades = Habilidad.objects.filter(perfil=perfil)
    referencias = Referencia.objects.filter(perfil=perfil)
    certificados = Certificado.objects.filter(perfil=perfil).order_by('-fecha_obtencion')

    contexto = {
        'perfil': perfil,
        'experiencias': experiencias,
        'habilidades': habilidades,
        'referencias': referencias,
        'certificados': certificados,
    }

    return render(request, 'cv/index.html', contexto)
