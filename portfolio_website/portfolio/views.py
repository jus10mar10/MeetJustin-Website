from django.shortcuts import render

pages = ['Home', 'About', 'Contact']

def Home(request):
    context = {
        'texts': ["Data Enthusiast",
                  "Code Lover",
                  "Chattanoogan",
                  "Finance Fanatic",
                  "Django Developer"]
    }
    current_page = 'Home'
    other_pages = [page for page in pages if page != current_page]
    return render(request, 'home.html', {"texts":context["texts"], "current_page":current_page, "other_pages":other_pages})

def About(request):
    current_page = 'About'
    other_pages = [page for page in pages if page != current_page]
    return render(request, 'coming_soon.html', {"current_page":current_page, "other_pages":other_pages})

def Contact(request):
    current_page = 'Coming Soon'
    other_pages = [page for page in pages if page != current_page]
    return render(request, 'coming_soon.html', {"current_page":current_page, "other_pages":other_pages})