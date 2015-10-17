from django.shortcuts import render
from .models import Resource


def start(request):
    return render(request, 'lighthouseapp/start.html')


def browse(request):
    resources = Resource.objects.order_by('category')
    return render(request,
                  'lighthouseapp/browse.html',
                  {'resources': resources})
