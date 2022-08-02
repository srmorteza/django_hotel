from django.shortcuts import render

from .models import Property


def property_list(request):
    property_list = Property.objects.all()
    template = 'property/property_list.html'
    context = {
        'property_list': property_list
    }
    return render(request, template, context)


def property_detail(request, id):
    property_detail = Property.objects.get(id=id)
    context = {
        'property_detail': property_detail
    }
    return render(request, 'property/property_detail.html', context)
