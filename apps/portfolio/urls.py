from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home, name="Home"),
    path("Home", views.Home, name="Home"),
    path("Portfolio", views.Portfolio, name="Portfolio"),
    path("Resources", views.Resources, name="Resources"),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
]