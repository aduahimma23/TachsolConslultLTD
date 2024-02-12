from django.shortcuts import render, get_object_or_404
from .forms import ContactForm
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from .models import Portfolio, Clients, Services, TeamMembers, About, ScopeofOpearation, Mission

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


# class Mission(TemplateView):
#     model = Mission
#     template_name = 'mainapp/mission.html'

def mission_view(request):
    mission = Mission.objects.first()

    return render(request, 'mainapp/mission.html', {'mission': mission})


# def portfolio_detail(request, portfolio_id):

#     portfolio = get_object_or_404(Portfolio, pk=portfolio_id)


def portfolio(request):
    portfolios = Portfolio.objects.all()

    return render(request, "mainapp/portfolio.html", {'portfolios': portfolios})

def client_view(request):
    clients = Clients.objects.all()

    return render(request, "mainapp/clients.html", {"clients": clients})

def about(request):
    abouts = About.objects.all()

    return render(request, 'mainapp/about.html', {'abouts': abouts})

def service(request, scope_pk):
    scope = ScopeofOpearation.objects.get(pk=scope_pk)
    services = Services.objects.filter(scope=scope)

    return render(request, 'mainapp/services.html', {'services': services})

def team(request, member_id):
   members = TeamMembers.objects.get(id=member_id)

   return render(request, 'mainapp/team.html', {'members': members})