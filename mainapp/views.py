from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView
from .models import Portfolio, Clients, Services

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
    portfolio = Portfolio.objects.first()
    context = {"portfolio": portfolio}

    return render(request, "mainapp/portfolio.html", context)

def client_view(request):
    clients = Clients.objects.all()

    return render(request, "mainapp/clients.html", {"clients": clients})

def about(request):
    return render(request, 'mainapp/about.html')

class ServicesView(ListView):
    model =  Services
    template_name = 'mainapp/services.html'
    context_object_name = 'services'

def team(request):
    # team = TeamMembers.objects.all()
    # context = {"team": team}

    return render(request, 'mainapp/team.html')