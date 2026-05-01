from django.db import models

class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='articulos/', blank=True, null=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.titulo


class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    resumen = models.TextField()
    imagen = models.ImageField(upload_to='noticias/', blank=True, null=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.titulo
