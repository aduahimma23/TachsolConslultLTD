from django.db import models

class Contact(models.Model):
    author = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(null=False, max_length=10)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Name {self.author}  : Date {self.created_date}"

class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio_images/', blank=True)
    title = models.CharField(max_length=100, blank=False, default="Mr")
    Name = models.CharField(default="Tachsol", max_length=50, blank=False)
    position = models.CharField(max_length=50, default="")
    content = models.TextField(max_length=1500, default="Tachsol Consult", blank=False)

    def __str__(self) -> str:
        return self.title, self.Name
    

class Clients(models.Model):
    clients_image = models.ImageField(upload_to='clients_image/', blank=True)
    clients_name = models.CharField(max_length=500, blank=False, default="@Tachsol Consult LTD")
    location = models.CharField(max_length=50, blank=False, default="Accra")
    description = models.CharField(blank=False, max_length=100, default="Tachsol")

    def __str__(self):
        return self.clients_name
    

class TeamMembers(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=100, default="Tachsol")
    position = models.CharField(max_length=50, default="Founder")
    contact = models.CharField(max_length=10, blank=False )
    meeting_hours = models.DateTimeField(null=True, default=0)

    def __str__(self):
        return self.name
    
class Services(models.Model):
    updated_by = models.CharField(max_length=50, default="Mr. Offei")
    content = models.TextField(max_length=1500, default="Enter the text here")
    description = models.CharField(max_length=100, default="We serve you better")


    def __str__(self):
        return self.updated_by

class About(models.Model):
    update_the_about_page = models.TextField(max_length=2000)
    location = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.update_the_about_page
    