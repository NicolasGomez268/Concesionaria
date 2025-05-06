from django.db import models

# Create your models here.

class Vehiculo(models.Model):
    ESTADO_CHOICES = [
        ('nuevo', 'Nuevo'),
        ('usado', 'Usado'),
    ]

    marca = models.CharField(max_length=100, blank=True, null=True)
    modelo = models.CharField(max_length=100, blank=True, null=True)
    año = models.IntegerField(blank=True, null=True)
    precio = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, blank=True, null=True)
    imagen_destacada = models.ImageField(upload_to='vehiculos/', blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    combustible = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    transmision = models.CharField(max_length=50, blank=True, null=True)
    kilometraje = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        verbose_name = 'Vehículo'
        verbose_name_plural = 'Vehículos'
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f"{self.marca} {self.modelo} {self.año}"

class ImagenVehiculo(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='vehiculos/adicionales/')
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['orden']
        verbose_name = 'Imagen Adicional'
        verbose_name_plural = 'Imágenes Adicionales'

    def __str__(self):
        return f"Imagen de {self.vehiculo} #{self.orden + 1}"
