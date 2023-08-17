from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Project

pages = ['Home', 'Portfolio', 'Resources']

def Home(request):
    context = {
        'texts': ["Data Enthusiast",
                  "Python Programmer",
                  "Chattanoogan",
                  "Finance Fanatic",
                  "Django Developer",
                  "Power Apps Creator",
                  "SQL Proficent",
                  "HTML and CSS",
                  "Excel Expert",
                  "Tableau User",]
    }
    current_page = 'Home'
    other_pages = [page for page in pages if page != current_page]
    return render(request, 'home.html', {"texts":context["texts"], "current_page":current_page, "other_pages":other_pages})

def Portfolio(request):
    current_page = 'Portfolio'
    other_pages = [page for page in pages if page != current_page]
    context = get_object_or_404(Project, pk=1)
    return render(request, 'detail.html', {"current_page":current_page, "other_pages":other_pages, "context":context})

def Resources(request):
    current_page = 'Resources'
    other_pages = [page for page in pages if page != current_page]
    return render(request, 'coming_soon.html', {"current_page":current_page, "other_pages":other_pages})

def project_detail(request, project_id):
    project = get_list_or_404(Project, pk=project_id)
    return render(request, 'portfolio/project_detail.html', {'project': project})
