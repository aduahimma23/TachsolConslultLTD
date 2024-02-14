from django.db import models
from django.core.exceptions import ValidationError

class Title(models.Model):
    MALE = 'Mr.'
    FEMALE_SINGLE = 'Ms.'
    FEMALE_MARRIED = 'Mrs.'

    CHOICES = [
        (MALE, 'Mr'),
        (FEMALE_SINGLE, 'Ms'),
        (FEMALE_MARRIED, 'Mrs'),
    ]
    
    gender = models.CharField(default='Mr', max_length=20, choices=CHOICES)

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title
    

class About(models.Model):
    title = models.CharField(max_length=150, default='About Tachsol Consultancy LTD')
    content = models.TextField()
    image = models.ImageField(upload_to='about_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

 
class ScopeOfOperation(models.Model):
    name = models.CharField(max_length=100, blank=False, default='Human Resource Development, Training, and Facilitation')

    def __str__(self):
        return self.name


class Services(models.Model):
    scope = models.ForeignKey(ScopeOfOperation, on_delete=models.CASCADE, related_name='services')
    activity = models.CharField(max_length=255, blank=False, default='Training Needs Assessment')
    description = models.TextField(max_length=255, blank=True, default='Short note about the activity')

    def __str__(self):
        return self.scope.name
    

class Testimonial(models.Model):
    title = models.CharField(max_length=5, choices=Title.CHOICES)
    author = models.CharField(max_length=100, default='Mr. Martin Offei')
    content = models.TextField(max_length=1500, default="Write the testimonial here")


class HomePage(models.Model):
    welcome_message = models.TextField()
    services = models.ManyToManyField(Services)
    projects = models.ManyToManyField(Project)
    testimonials = models.ManyToManyField(Testimonial)

    def __str__(self):
        return "Homepage Content"


class Portfolio(models.Model):
    title = models.CharField(max_length=5, choices=Title.CHOICES)
    name = models.CharField(max_length=50, default="Tachsol", blank=False)
    email = models.EmailField(default="tachsol.km@gmail.com", blank=False)
    image = models.ImageField(upload_to='portfolio_images/', blank=True)
    content = models.TextField(max_length=1500, default="Tachsol Consult", blank=False)
    phone_number = models.CharField(max_length=15, default="+1234567890", blank=False, help_text="Enter in the format: +1234567890")
    work_experience = models.TextField(max_length=1000, blank=False, default='legal practitioner')
    educational_background = models.TextField(max_length=500, default='Write something about your educational background')


class EmploymentRecord(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    year = models.DateField(auto_now=False)
    position = models.CharField(max_length=50, default="", blank=True)
    duties = models.TextField(max_length=500, default='Overall management')



    def __str__(self):
        return f'{self.portfolio.title}. {self.portfolio.name}'

    def clean(self):
        if not self.portfolio.email:
            raise ValidationError("Email field cannot be empty")

        if not self.portfolio.phone_number.startswith('+'):
            raise ValidationError("Phone number must start with a plus sign (+)")
        

class Clients(models.Model):
    image = models.ImageField(upload_to='clients_image/', blank=False)
    name = models.CharField(max_length=500, default="@Tachsol Consult LTD", blank=False)
    location = models.CharField(max_length=50, default="Accra", blank=False)
    description = models.CharField(max_length=100, default="Tachsol", blank=False)
    contact = models.CharField(max_length=15, default="+233208157526", blank=False, help_text="Enter in the format: +1234567890")
    website_link = models.URLField(default="http://tachsol.com", blank=True)
    email = models.EmailField(default="info@tachsol.com", blank=False)
    sector_of_work = models.CharField(max_length=100, default='Banking')

    def __str__(self):
        return self.name

    def clean(self):
        if not self.contact.startswith('+'):
            raise ValidationError("Contact number must start with a plus sign (+)")


class TeamMembers(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=100, default="Tachsol")
    position = models.CharField(max_length=50, default="Founder")
    email = models.EmailField(default="info@tachsol.com")

    def __str__(self):
        return f'{self.name} {self.email}'
    

class Mission(models.Model):
    created_at = models.DateField(auto_now_add=True)
    content = models.TextField(max_length=2000)

    def __str__(self):
        return f'Created {self.created_at}'