from django.shortcuts import render

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
                  "HTML and CSS Aware",
                  "Excel Expert",
                  "Tableau User",]
    }
    current_page = 'Home'
    other_pages = [page for page in pages if page != current_page]
    return render(request, 'home.html', {"texts":context["texts"], "current_page":current_page, "other_pages":other_pages})

def Portfolio(request):
    current_page = 'Portfolio'
    other_pages = [page for page in pages if page != current_page]
    return render(request, 'coming_soon.html', {"current_page":current_page, "other_pages":other_pages})

def Resources(request):
    current_page = 'Resources'
    other_pages = [page for page in pages if page != current_page]
    return render(request, 'coming_soon.html', {"current_page":current_page, "other_pages":other_pages})