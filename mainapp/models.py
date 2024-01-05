from django.db import models

class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio_images/', blank=True)
    title = models.CharField(max_length=100, blank=False, default="Mr")
    Name = models.CharField(default="Tachsol", max_length=50, blank=False)
    position = models.CharField(max_length=50, default="")
    content = models.TextField(max_length=1500, default="Tachsol Consult", blank=False)

    def __str__(self):
        return f' {self.title}. {self.Name}'
    

class Clients(models.Model):
    clients_image = models.ImageField(upload_to='clients_image/', blank=False)
    clients_name = models.CharField(max_length=500, blank=False, default="@Tachsol Consult LTD")
    location = models.CharField(max_length=50, blank=False, default="Accra")
    contact = models.CharField(max_length=20)
    description = models.CharField(blank=False, max_length=100, default="Tachsol")
    ulr_link = models.URLField(default="tachsol.com")

    def __str__(self):
        return self.clients_name
    

class TeamMembers(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=100, default="Tachsol")
    position = models.CharField(max_length=50, default="Founder")

    def __str__(self):
        return self.name
    
class Services(models.Model):
    name = models.CharField(max_length=100, unique=False, blank=False, default='Tachsol')
    updated_by = models.CharField(max_length=50, default="Mr. Offei", blank=False)
    service_image = models.ImageField(upload_to='Service_images/', blank=False, default='static/images/service/default_image.png')
    content = models.TextField(max_length=1500, default="Enter the text here")
    description = models.CharField(max_length=100, default="We serve you better")

    def __str__(self):
        return self.name
    