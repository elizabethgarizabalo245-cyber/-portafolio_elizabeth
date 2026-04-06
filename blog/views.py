from django.shortcuts import render
from .models import Project

def home(request):
    try:
        projects = Project.objects.all()
    except:
        projects = []
    return render(request, 'home.html', {'projects': projects})

from django.contrib.auth.models import User

def crear_admin_seguro():
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@gmail.com', '1234')