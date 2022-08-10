from django.core.mail import send_mail, BadHeaderError
from django.core.mail import send_mail as sm
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm
from .models import ContactDetail


# Create your views here.

def send_mail(request):
    contactdetail = ContactDetail.objects.last()

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            subject = contact_form.cleaned_data['subject']
            from_email = contact_form.cleaned_data['from_email']
            message = contact_form.cleaned_data['message']
            try:
                sm(subject, message, from_email, ['test@gmail.com'])
            except BadHeaderError:
                return HttpResponse('invalid header')

            return redirect('contact:success')
    else:
        contact_form = ContactForm()

    context = {
        'contactdetail': contactdetail,
        'contact_form': contact_form
    }
    return render(request, 'contact/contact.html', context)


def success(request):
    return HttpResponse('message sent successfully')
