from django.shortcuts import render

def home(request):
    projects = [
        
        {
            "title": "Frontend Proyecto",
            "description": "Aplicación frontend desarrollada con JavaScript.",
            "image": "/static/img/frontend.png",
            "url": "https://github.com/elizabethgarizabalo245-cyber/frontend_proyecto"
        },
        {
            "title": "Proyecto Web Java",
            "description": "Aplicación web desarrollada en Java.",
            "image": "/static/img/Proyecto Web Java.png",
            "url": "https://github.com/elizabethgarizabalo245-cyber/ProyectoWebNuevo2"
        },
        {
            "title": "Proyecto Web",
            "description": "Proyecto web desarrollado en Java con funcionalidades básicas.",
            "image": "/static/img/Proyecto Web.png",
            "url": "https://github.com/elizabethgarizabalo245-cyber/proyecto-web"
        },
        {
            "title": "Proyecto Django",
            "description": "API desarrollada con Node.js y Express para evidencia académica.",
            "image": "/static/img/API Proyecto.png",
            "url": "https://github.com/elizabethgarizabalo245-cyber/django-react-crud"
        }
    ]

    return render(request, 'home.html', {"projects": projects})