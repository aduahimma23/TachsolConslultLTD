from django.urls import path
from . import views

app_name = "mainapp"

urlpatterns = [
    path('home/', views.homepage, name='home'),
    path('about/', views.about, name='about'),
    path('mission/', views.Mission.as_view(), name='mission'),
    path('contact/', views.contact_us, name='contact'),
    path('portfolio/', views.portFolio, name='portfolio'),
    path('client/', views.client_view, name='client'),
    path('services/', views.ServicesView.as_view(), name="services"),
    path('team/', views.team, name='team')
]
