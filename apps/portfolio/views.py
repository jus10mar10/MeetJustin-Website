from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Post
from django.views import View
from django.conf import settings
from django.shortcuts import redirect
from .forms import UserRegisterForm, ContactForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from apps.account.models import UserProfile, Avatar
from django.http import HttpResponseRedirect
from .models import Contact

def Home(request):
    context = {
        'texts': ["Data Enthusiast",
                  "Python",
                  "Chattanoogan",
                  "Finance Fanatic",
                  "Django Developer",
                  "SQL",
                  "HTML and CSS",
                  "Excel Expert",
                  "Tableau User",]
    }
    current_page = 'Home'
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')

            # Create Contact instance
            contact = Contact(name=name, email=email, message=message)
            contact.save()

            # Redirect to the same page or a 'thank you' page after successful submission
            return redirect('/')  # Use your own URL name or path for redirection

    return render(request, 'home.html', {"texts":context["texts"], "current_page":current_page})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    current_page = post.type.capitalize()
    posts = Post.objects.filter(type=post.type, is_published=True).order_by('-date') 
    #remove current post from posts
    posts = [p for p in posts if p.id != post_id]
    return render(request, 'detail.html', {"current_page":current_page, "post":post, "posts":posts})

class BaseGalleryView(View):
    current_page = None
    page_description = None
    post_type = None

    def get(self, request, *args, **kwargs):
        posts = Post.objects.filter(type=self.post_type, is_published=True).order_by('-date')
        context = {
            "current_page": self.current_page,
            "posts": posts,
            "page_description": self.page_description
        }
        return render(request, 'gallery.html', context)
    
class Portfolio(BaseGalleryView):
    current_page = 'Portfolio'
    page_description = "Explore my portfolio to see the data-driven projects I've tackled and the solutions I've crafted."
    post_type = 'portfolio'


class Blog(BaseGalleryView):
    current_page = 'Blog'
    page_description = "Blog containing my thoughts on data, finance, and technology."
    post_type = 'blog'

def search_view(request):
    query = request.GET.get('q', '')
    posts = Post.objects.filter(title__contains=query, content__contains=query, is_published=True).order_by('-date')
    current_page = 'Search'
    search = '<span id="search-icon">🔍</span>'
    return render(request, 'gallery.html', {'posts': posts, 'current_page': current_page, 'search': search})

def error_404_view(request, exception):
    return render(request, '404.html')

def signup(request):
    if request.method == 'POST':  # Form was submitted
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # This will create the user
            # Redirect to a success page.
            avatar = Avatar.objects.get(name='default')
            user = User.objects.get(username=form.cleaned_data['username'])
            user_profile = UserProfile.objects.create(user=user)
            user_profile.selected_avatar = avatar
            user_profile.save()
            return redirect('/signin/')  # replace 'some-success-url' with an actual URL pattern name
            
    else:
        form = UserRegisterForm()  # An unbound form, for GET request

    return render(request, 'signup.html', {'form': form})

# views.py
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/')  # Redirect to the desired page after login
        else:
            # Invalid login credentials
            messages.error(request, 'Invalid username or password.')

    return render(request, 'signin.html')

def user_logout(request):
    logout(request)
    return redirect('/')  # You can redirect to any named URL pattern

def resources(request):
    return render(request, 'coming_soon.html')