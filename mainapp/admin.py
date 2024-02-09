from django.contrib import admin
from .models import (Portfolio, Clients, TeamMembers, Services, About,
                        EmploymentRecord, ScopeofOpearation, Testimonial, Project, HomePage)

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'updated_at')


class ClientsAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'sector_of_work')
    search_fields = ('name', 'location', 'sector_of_work')
    list_filter = ('location', 'sector_of_work')

admin.site.register(Clients, ClientsAdmin)


class EmploymentRecordInline(admin.TabularInline):
    model = EmploymentRecord


class PortfolioAdmin(admin.ModelAdmin):
    inlines = [EmploymentRecordInline,]
    list_display = ['title', 'name', 'email']
    search_fields = ['title', 'name', 'email']

admin.site.register(Portfolio, PortfolioAdmin)


class TeamMembersAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'email']
    search_fields = ['name', 'position', 'email']

admin.site.register(TeamMembers)


class ServicesInline(admin.TabularInline):
    model = Services

class ScopeofOpearationAdmin(admin.ModelAdmin):
    inlines = [ServicesInline,]
    list_display = ['name', 'description']
    search_fields = ['name']

admin.site.register(ScopeofOpearation, ScopeofOpearationAdmin)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'start_date', 'end_date')
    list_filter = ('start_date', 'end_date')
    search_fields = ('title', 'description')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'content')


@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    filter_horizontal = ('services', 'projects', 'testimonials')

admin.site.site_header = 'Tachsol Consultancy LTD'