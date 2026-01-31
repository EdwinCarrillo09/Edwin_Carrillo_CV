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
        'Perfil',
        on_delete=models.CASCADE,
        related_name='ventas_garaje'
    )

    nombre_producto = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    estado_producto = models.CharField(
        max_length=50,
        choices=[
            ('Nuevo', 'Nuevo'),
            ('Usado', 'Usado'),
            ('Semi-nuevo', 'Semi-nuevo')
        ]
    )
    valor_bien = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='venta_garaje/', blank=True, null=True)
    activo_front = models.BooleanField(default=True)

    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_producto
