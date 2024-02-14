from django.urls import path
from . import views

app_name = "mainapp"

urlpatterns = [
    path('home/', views.homepage, name='home'),
    path('about/', views.about, name='about'),
    path('mission/', views.mission_view, name='mission'),
    path('contact/', views.contact_us, name='contact'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('client/', views.client_view, name='client'),
    path('service/', views.service, name="service"),
    path('team/', views.team, name='team'),
]
