from django.shortcuts import render
from .models import Resource
#from .forms import ResourceForm

def start(request):
     return render(request, 'lighthouseapp/start.html')

# Create your views here.


def browse_page(request):
    return render(request, 'lighthouseapp/browse_page.html', {})
