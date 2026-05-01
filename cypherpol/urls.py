
from django.contrib import admin
from django.urls import path
from noticias import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('articulo/<int:id>',views.detalle_articulo, name='detalle_articulo'),
    path('noticia/<int:id>', views.detalle_noticia, name='detalle_noticia')
]
