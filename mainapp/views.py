from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from .models import Portfolio, Clients, TeamMembers, Services

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
    team = TeamMembers.objects.all()
    context = { "team": team}

    return render(request, 'mainapp/index.html', context)


class Mission(TemplateView):
    template_name = 'mainapp/mission.html'

def portFolio(request):
    portfolio = Portfolio.objects.first()
    context = {"portfolio": portfolio}

    return render(request, "mainapp/portfolio.html", context)

def ourClients(request):
    clients = Clients.objects.all()
    context = {"clients": clients}

    return render(request, "mainapp/clients.html", context)

def about(request):
    return render(request, 'mainapp/about.html')

def services(request):
    service = Services.objects.all()
    context = {"services": service}

    return render(request, 'mainapp/services.html', context)

def team(request):
    team = TeamMembers.objects.all()
    context = {"team": team}

    return render(request, 'mainapp/team.html', context)