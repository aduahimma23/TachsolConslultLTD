from django import forms
from django.core.mail import send_mail
import logging

logger = logging.getLogger(__name__)

class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email', required=True)
    message = forms.CharField(max_length=600, widget=forms.Textarea)

    def send_mail(self):
        logger.info('sending email to tachsol consultancy LTD')
        message = "form: {0}\n{1}".format(
            self.cleaned_data["name"],
            self.cleaned_data["email"],
            self.cleaned_data["message"],
        )
        send_mail(
            'site message',
            message, 'site@tachsolconsultLTD.com',
            ['tachsolconsultLTD.com'],
            fail_silently = False,
        )