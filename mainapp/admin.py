from django.contrib import admin
from .models import Portfolio, Clients, TeamMembers, Services

admin.site.register(Portfolio)
admin.site.register(Clients)
admin.site.register(TeamMembers)
admin.site.register(Services)