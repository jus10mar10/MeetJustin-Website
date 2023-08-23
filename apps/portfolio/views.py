from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Post
from django.views import View

pages = ['Home', 'Portfolio', 'Resource']

def Home(request):
    context = {
        'texts': ["Data Enthusiast",
                  "Python Programmer",
                  "Chattanoogan",
                  "Finance Fanatic",
                  "Django Developer",
                  "Power Apps Creator",
                  "SQL User",
                  "HTML and CSS",
                  "Excel Expert",
                  "Tableau User",]
    }
    current_page = 'Home'
    other_pages = [page for page in pages if page != current_page]
    return render(request, 'home.html', {"texts":context["texts"], "current_page":current_page, "other_pages":other_pages})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    current_page = post.type.capitalize()
    other_pages = [page for page in pages if page != current_page]
    return render(request, 'detail.html', {"current_page":current_page, "other_pages":other_pages, "post":post})

class BaseGalleryView(View):
    current_page = None
    page_description = None
    post_type = None

    def get(self, request, *args, **kwargs):
        other_pages = [page for page in pages if page != self.current_page]
        posts = Post.objects.filter(type=self.post_type, is_published=True)
        context = {
            "current_page": self.current_page,
            "other_pages": other_pages,
            "posts": posts,
            "page_description": self.page_description
        }
        return render(request, 'gallery.html', context)
    
class Portfolio(BaseGalleryView):
    current_page = 'Portfolio'
    page_description = "Explore my portfolio to see the data-driven projects I've tackled and the solutions I've crafted."
    post_type = 'portfolio'


class Resource(BaseGalleryView):
    current_page = 'Resource'
    page_description = "Some helpful resources to help you on your tech journey."
    post_type = 'resource'

def search_view(request):
    query = request.GET.get('q', '')
    posts = Post.objects.filter(title__contains=query, is_published=True)
    current_page = 'Search🔍'
    other_pages = [page for page in pages if page != current_page]
    return render(request, 'gallery.html', {'posts': posts, 'current_page': current_page, 'other_pages': other_pages})
