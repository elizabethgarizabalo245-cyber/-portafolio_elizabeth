from django.shortcuts import render
from .models import Project

def home(request):
    try:
        projects = Project.objects.all()
    except:
        projects = []
    return render(request, 'home.html', {'projects': projects})