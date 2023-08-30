from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Post
from django.views import View

def Home(request):
    context = {
        'texts': ["Data Enthusiast",
                  "Python Programmer",
                  "Chattanoogan",
                  "Finance Fanatic",
                  "Django Developer",
                  "SQL",
                  "HTML and CSS",
                  "Excel Expert",
                  "Tableau User",]
    }
    current_page = 'Home'
    return render(request, 'home.html', {"texts":context["texts"], "current_page":current_page})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    current_page = post.type.capitalize()
    return render(request, 'detail.html', {"current_page":current_page, "post":post})

class BaseGalleryView(View):
    current_page = None
    page_description = None
    post_type = None

    def get(self, request, *args, **kwargs):
        posts = Post.objects.filter(type=self.post_type, is_published=True)
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
    posts = Post.objects.filter(title__contains=query, content__contains=query, is_published=True)
    current_page = 'Search'
    search = '<span id="search-icon">🔍</span>'
    return render(request, 'gallery.html', {'posts': posts, 'current_page': current_page, 'search': search})
