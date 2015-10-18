from django.shortcuts import render
from .models import Resource

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
            my_result = Resource.objects.filter(aspiration=cd['aspiration'],
                                                group=cd['group'],
                                                level=cd['level'])
            return render(request,
                          'lighthouseapp/result.html',
                          {'results': my_result})
        else:
            form = ResourceFilterForm()
            return render(request, 'lighthouseapp/filter.html', {'form': form})
    else:
        form = ResourceFilterForm()
        return render(request, 'lighthouseapp/filter.html', {'form': form})


def detail(request, primary_key):
    resource = Resource.objects.get(pk=primary_key)
    return render(request, 'lighthouseapp/detail.html', {'resource': resource})
