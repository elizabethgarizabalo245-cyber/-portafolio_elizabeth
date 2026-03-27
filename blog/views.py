from django.shortcuts import render, get_object_or_404
from .models import Post

def crear_datos(request):
    Post.objects.create(
        title="Mi primer proyecto",
        description="Este es mi proyecto en producción",
    )
    return HttpResponse("Datos creados")