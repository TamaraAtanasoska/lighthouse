from django.shortcuts import render
from .models import Resource
#from .forms import ResourceForm

def start(request):
     return render(request, 'lighthouseapp/start.html')

# Create your views here.
