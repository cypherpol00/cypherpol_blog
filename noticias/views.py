from django.shortcuts import render, get_object_or_404
from .models import Articulo, Noticia

def home(request):
    articulos = Articulo.objects.all().order_by('-fecha_publicacion')
    noticias = Noticia.objects.all().order_by('-fecha_publicacion')
    return render(request, 'noticia/index.html', {
        'articulos': articulos,
        'noticias': noticias
    })

def detalle_articulo(request, id):
    articulo = get_object_or_404(Articulo, id=id)
    return render(request, 'noticia/detalle_articulo.html', {'articulo': articulo})

def detalle_noticia(request, id):
    noticia = get_object_or_404(Noticia, id=id)
    return render(request, 'noticia/detalle_noticia.html', {'noticia': noticia})