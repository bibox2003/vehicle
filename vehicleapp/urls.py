from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clients/', views.clients, name='clients'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),   
    path('contact/', views.contact, name='contact'),

    # Authentication
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
]
