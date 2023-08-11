from django.shortcuts import render

def home(request):
    context = {
        'texts': ["Data Enthusiast",
                  "Code Lover",
                  "Chattanoogan",
                  "Finance Fanatic",
                  "Django Developer"]
    }
    return render(request, 'base.html', context)
