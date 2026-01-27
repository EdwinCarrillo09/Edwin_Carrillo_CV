from django.shortcuts import render
# 1. Agrega 'Referencia' y 'Certificado' a la importación
from .models import Perfil, Experiencia, Habilidad, Referencia, Certificado

def ver_cv(request):    
    # Obtenemos el primer perfil
    perfil = Perfil.objects.first()
    
    # 2. Filtramos para que solo traiga los datos de ESE perfil específico
    # Esto evita que se mezclen datos si luego tienes más de un perfil
    experiencias = Experiencia.objects.filter(perfil=perfil)
    habilidades = Habilidad.objects.filter(perfil=perfil)
    referencias = Referencia.objects.filter(perfil=perfil) # <-- Nueva línea
    certificados = Certificado.objects.filter(perfil=perfil) # <-- Agregado también
    
    contexto = {
        'perfil': perfil,
        'experiencias': experiencias,
        'habilidades': habilidades,
        'referencias': referencias, 
        'certificados': certificados, 
    }
    return render(request, 'cv/index.html', contexto)