from django.urls import path
from . import views
from .views import Portfolio, Blog


urlpatterns = [
    path("", views.Home, name="Home"),
    path("Home", views.Home, name="Home"),
    path('Portfolio/', Portfolio.as_view(), name='Portfolio'),
    path('Blog/', Blog.as_view(), name='Blog'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('search_view/', views.search_view, name='search_view'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('account/', views.account, name='account'),
    path('resources/', views.resources, name='resources'),
]