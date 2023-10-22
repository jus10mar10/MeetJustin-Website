from django.urls import path
from . import views

urlpatterns = [
    path('account/', views.account, name='account'),
    path('delete_account/', views.delete_account, name='delete_account'),
]
