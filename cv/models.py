from django.utils import timezone
from django.db import models

class Perfil(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    profesion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100, blank=True)
    pais = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True)
    bio = models.TextField()
    nacionalidad = models.CharField(max_length=100, blank=True, null=True)
    lugarnacimiento = models.CharField(max_length=100, blank=True, null=True)
    fechanacimiento = models.DateField(null=True, blank=True) 
    numerocedula = models.CharField(max_length=20, blank=True, null=True)
    sexo = models.CharField(max_length=20, blank=True, null=True)
    estadocivil = models.CharField(max_length=50, blank=True, null=True)
    licenciaconducir = models.CharField(max_length=50, blank=True, null=True)
    telefonoconvencional = models.CharField(max_length=20, blank=True, null=True)
    direcciondomiciliaria = models.CharField(max_length=255, blank=True, null=True)
    tiposangre = models.CharField(max_length=10, blank=True, null=True)
    direcciontrabajo = models.CharField(max_length=255, blank=True, null=True)
    foto = models.ImageField(upload_to='perfil/', null=True, blank=True) 

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Experiencia(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='experiencias', null=True)
    empresa = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    
    # CAMBIO: Usamos DateField para ordenamiento cronológico real
    inicio = models.DateField()
    fin = models.DateField(null=True, blank=True) # Si es null, asumiremos "Actualidad"
    
    logros = models.TextField()

    class Meta:
        # Esto garantiza el orden cronológico descendente (más reciente arriba)
        ordering = ['-inicio']

    def __str__(self):
        return f"{self.cargo} en {self.empresa}"


class Certificado(models.Model):
    TIPO_CHOICES = (
        ('curso', 'Curso'),
        ('reconocimiento', 'Reconocimiento'),
    )

    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    institucion = models.CharField(max_length=200)
    fecha_obtencion = models.DateField()
    archivo = models.FileField(upload_to='certificados/')
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)

   
    total_horas = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="Solo para cursos"
    )

    class Meta:
        ordering = ['-fecha_obtencion']

    def __str__(self):
        return self.titulo



class Habilidad(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='habilidades', null=True)
    CATEGORIA_CHOICES = [('T', 'Técnica'), ('B', 'Blanda')]
    nombre = models.CharField(max_length=50)
    categoria = models.CharField(max_length=1, choices=CATEGORIA_CHOICES, default='T')

    def __str__(self):
        return f"{self.nombre} ({self.get_categoria_display()})"


class Referencia(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='referencias', null=True)
    nombre = models.CharField(max_length=150, verbose_name="Nombre de la Referencia")
    telefono = models.CharField(max_length=20, verbose_name="Número de Celular")
    email = models.EmailField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre}"
    
class VentaGaraje(models.Model):
    perfil = models.ForeignKey(
        Perfil,
        on_delete=models.CASCADE,
        related_name='ventas_garaje'
    )

    nombre_producto = models.CharField(max_length=100)
    descripcion = models.TextField()
    estado_producto = models.CharField(max_length=50)
    valor_bien = models.DecimalField(max_digits=10, decimal_places=2)

    fecha_publicacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre_producto

from django.db import models
from .models import Perfil   # si Perfil está en el mismo archivo, ignora esta línea


from django.db import models


class ProductoAcademico(models.Model):
    idproductoacademico = models.AutoField(primary_key=True)

    perfil = models.ForeignKey(
        'Perfil',
        on_delete=models.CASCADE,
        db_column='idperfilconqueestaactivo',
        related_name='productos_academicos'
    )

    nombrerecurso = models.CharField(max_length=100)
    clasificador = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    activarparaqueseveaenfront = models.BooleanField(default=True)

    class Meta:
        db_table = 'productosacademicos'

    def __str__(self):
        return self.nombrerecurso
class ProductoLaboral(models.Model):
    perfil = models.ForeignKey(
        Perfil,
        on_delete=models.CASCADE,
        related_name='productos_laborales'
    )

    nombre_recurso = models.CharField(max_length=100)
    clasificador = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_recurso




