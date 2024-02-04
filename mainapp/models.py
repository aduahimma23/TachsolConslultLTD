from django.db import models
from django.core.exceptions import ValidationError

class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio_images/', blank=True)
    title = models.CharField(max_length=100, default="Mr", blank=False)
    name = models.CharField(max_length=50, default="Tachsol", blank=False)
    position = models.CharField(max_length=50, default="", blank=True)
    email = models.EmailField(default="tachsol.km@gmail.com")
    content = models.TextField(max_length=1500, default="Tachsol Consult", blank=False)

    def __str__(self):
        return f'{self.title}. {self.name}'

    def clean(self):
        if not self.email:
            raise ValidationError("Email field cannot be empty")

class Clients(models.Model):
    clients_image = models.ImageField(upload_to='clients_image/', blank=False)
    clients_name = models.CharField(max_length=500, default="@Tachsol Consult LTD", blank=False)
    location = models.CharField(max_length=50, default="Accra", blank=False)
    description = models.CharField(max_length=100, default="Tachsol", blank=False)
    client_contact = models.IntegerField(default=233208157526)
    url_link = models.URLField(default="http://tachsol.com")

    def __str__(self):
        return self.clients_name

    def clean(self):
        if not self.client_contact:
            raise ValidationError("Client contact field cannot be empty")

class TeamMembers(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=100, default="Tachsol")
    position = models.CharField(max_length=50, default="Founder")
    contact = models.IntegerField(default=233208157526)

    def __str__(self):
        return self.name

class Services(models.Model):
    name = models.CharField(max_length=100, default='Tachsol', blank=False)
    updated_by = models.CharField(max_length=50, default="Mr. Offei", blank=False)
    service_image = models.ImageField(upload_to='Service_images/', default='static/images/service/default_image.png', blank=False)
    content = models.TextField(max_length=1500, default="Enter the text here", blank=False)
    description = models.CharField(max_length=100, default="We serve you better", blank=False)

    def __str__(self):
        return self.name
