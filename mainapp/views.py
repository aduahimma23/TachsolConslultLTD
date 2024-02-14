from django.shortcuts import render, get_object_or_404
from .forms import ContactForm
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from .models import Portfolio, Clients, Services, TeamMembers, About, ScopeOfOperation, Mission, HomePage

def contact_us(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_mail()
            return HttpResponseRedirect('/')
    else:
        form = ContactForm()

    return render(request, 'mainapp/contact_us.html', {'form': form})

def homepage(request):
    home_pages = HomePage.objects.all()
    return render(request, 'mainapp/index.html', {'home_pages': home_pages})

def mission_view(request):
    mission = Mission.objects.first()

    return render(request, 'mainapp/mission.html', {'mission': mission})

def portfolio(request):
    portfolios = Portfolio.objects.all()

    return render(request, "mainapp/portfolio.html", {'portfolios': portfolios})

def client_view(request):
    clients = Clients.objects.all()

    return render(request, "mainapp/clients.html", {"clients": clients})

def about(request):
    abouts = About.objects.all()

    return render(request, 'mainapp/about.html', {'abouts': abouts})

def service(request):
    scopes = ScopeOfOperation.objects.all()

    return render(request, 'mainapp/services.html', {'scopes': scopes})

def team(request):
   members = TeamMembers.objects.all()

   return render(request, 'mainapp/team.html', {'members': members})