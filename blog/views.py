from django.shortcuts import render

def home(request):
    projects = [
       
        {
            "title": "Diseño de Servicios Web",
            "description": "Proyecto en JavaScript enfocado en el diseño de servicios web.",
            "image": "https://via.placeholder.com/300",
            "url": "https://github.com/elizabethgarizabalo245-cyber/dise-o_serviciosweb.git"
        },
        {
            "title": "Frontend Proyecto",
            "description": "Aplicación frontend desarrollada con JavaScript.",
            "image": "https://via.placeholder.com/300",
            "url": "https://github.com/elizabethgarizabalo245-cyber/frontend_proyecto.git"
        },
        {
            "title": "Proyecto Web Java",
            "description": "Aplicación web desarrollada en Java.",
            "image": "https://via.placeholder.com/300",
            "url": "https://github.com/elizabethgarizabalo245-cyber/ProyectoWebNuevo2.git"
        },
        {
            "title": "Proyecto Web",
            "description": "Proyecto web desarrollado en Java con funcionalidades básicas.",
            "image": "https://via.placeholder.com/300",
            "url": "https://github.com/elizabethgarizabalo245-cyber/proyecto-web.git"
        },
        {
            "title": "API Proyecto",
            "description": "API desarrollada con Node.js y Express para evidencia académica.",
            "image": "https://via.placeholder.com/300",
            "url": "https://github.com/elizabethgarizabalo245-cyber/api-proyecto..git"
        }
    ]
    return render(request, 'home.html', {"projects": projects})