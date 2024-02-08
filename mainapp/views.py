from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from .models import Portfolio, Clients, Services, TeamMembers

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
    return render(request, 'mainapp/index.html')


class Mission(TemplateView):
    template_name = 'mainapp/mission.html'

def portFolio(request):
    portfolios = Portfolio.objects.all

    return render(request, "mainapp/portfolio.html", {'portfolios': portfolios})

def client_view(request):
    clients = Clients.objects.all()

    return render(request, "mainapp/clients.html", {"clients": clients})

def about(request):
    return render(request, 'mainapp/about.html')

def services(request):
    services = Services.objects.all()
    return render(request, 'mainapp/services.html', {'services': services})

def team(request, member_id):
   members = TeamMembers.objects.get(id=member_id)

   return render(request, 'mainapp/team.html', {'members': members})