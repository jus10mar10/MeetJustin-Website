from django.urls import path
from . import views
from .views import Portfolio, Resource

urlpatterns = [
    path("", views.Home, name="Home"),
    path("Home", views.Home, name="Home"),
    path('Portfolio/', Portfolio.as_view(), name='portfolio'),
    path('Resource/', Resource.as_view(), name='resource'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
]