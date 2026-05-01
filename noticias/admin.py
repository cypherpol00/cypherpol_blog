from django.contrib import admin
from .models import Articulo, Noticia

@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_publicacion')
    search_fields = ('titulo', 'autor')
    list_filter = ('fecha_publicacion',)

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_publicacion')
    search_fields = ('titulo', 'autor')
    list_filter = ('fecha_publicacion',)

