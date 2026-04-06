from django.contrib.auth.models import User
from django.http import HttpResponse

def crear_admin(request):
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@gmail.com', '1234')
        return HttpResponse("Admin creado")
    return HttpResponse("Ya existe")