from django.shortcuts import render

from .models import About


# Create your views here.
def aboutus(request):
    about = About.objects.last()
    context = {
        'about': about
    }
    return render(request, 'about/about.html', context)
