from django.shortcuts import render

def home(request):
    projects = [
        {
            "title": "Diseño de Servicios Web",
            "description": "Proyecto en JavaScript enfocado en el diseño de servicios web.",
            "image": "/static/img/Diseño de Servicios Web.png",
            "url": "https://github.com/elizabethgarizabalo245-cyber/dise-o_serviciosweb"
        },
        {
            "title": "Frontend Proyecto",
            "description": "Aplicación frontend desarrollada con JavaScript.",
            "image": "/static/img/Frontend Proyectos.png",
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
            "title": "API Proyecto",
            "description": "API desarrollada con Node.js y Express para evidencia académica.",
            "image": "/static/img/API Proyecto.png",
            "url": "https://github.com/elizabethgarizabalo245-cyber/api-proyecto"
        }
    ]

    return render(request, 'home.html', {"projects": projects})