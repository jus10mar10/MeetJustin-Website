from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Project
from .models import Resource

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
    page_description = "Explore my portfolio to see the data-driven projects I've tackled and the solutions I've crafted."
    other_pages = [page for page in pages if page != current_page]
    projects = get_list_or_404(Project)
    return render(request, 'gallery.html', {"current_page":current_page, "other_pages":other_pages, "projects":projects, "page_description":page_description})

def Resources(request):
    current_page = 'Resources'
    page_description = "Some helpful resources to help you on your tech journey."
    other_pages = [page for page in pages if page != current_page]
    projects = get_list_or_404(Resource)
    return render(request, 'resource.html', {"current_page":current_page, "other_pages":other_pages, "projects":projects})

def project_detail(request, project_id):
    current_page = 'Portfolio'
    other_pages = [page for page in pages if page != current_page]
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'detail.html', {"current_page":current_page, "other_pages":other_pages, "project":project})
