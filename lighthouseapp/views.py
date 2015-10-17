from django.shortcuts import render
from .models import Resource

import django_filters
from .forms import ResourceFilterForm


def start(request):
    return render(request, 'lighthouseapp/start.html')


def browse(request):
    resources = Resource.objects.order_by('category')
    return render(request,
                  'lighthouseapp/browse.html',
                  {'resources': resources})


def resource_filter(request):
	if request.method == 'POST':		
		form = ResourceFilterForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			result = Resource.objects.filter(aspiration = cd.aspiration)
			return redirect (request, 'lighthouseapp/result.html', {'result' : result})
		else:
			form = ResourceFilterForm()
			return render(request, 'lighthouseapp/filter.html', {'form': form})
	else:
		form = ResourceFilterForm()
		return render(request, 'lighthouseapp/filter.html', {'form': form})
     

def result(request):
	return render(request, 'lighthouseapp/result.html')







# Create your views here.

