import json
import requests

from django.shortcuts import render
from .models import Resource
from .forms import ResourceFilterForm


def start(request):
    return render(request, 'lighthouseapp/start.html')


def browse(request):
    resources = Resource.objects.order_by('category')
    # Add maps
    map_url = 'https://geocoder.cit.api.here.com/6.2/geocode.json'
    # map_url = 'https://image.maps.cit.api.here.com/mia/1.6/mapview'
    params = {
        'app_id': '6d0g57ZEuwQh6BsEX8SZ',
        'app_code': 'Ad6FxUzEnSS3PMyXfdCJWA',
        }
    # How to optimize this?
    for resource in resources:
        country = str(resource.country.name)
        params['country'] = country
        response = requests.get(map_url, params=params)
        json_response = json.loads(response.text)
        results = json_response['Response']['View'][0]['Result']
        map_view = results[0]['Location']['MapView']
        bottom_right_lat = map_view['BottomRight']['Latitude']
        bottom_right_lon = map_view['BottomRight']['Longitude']
        top_left_lat = map_view['TopLeft']['Latitude']
        top_left_lon = map_view['TopLeft']['Longitude']
    import ipdb
    ipdb.set_trace()
    return render(request,
                  'lighthouseapp/browse.html',
                  {
                      'resources': resources,
                      'bottom_right_lat': bottom_right_lat,
                      'bottom_right_lon': bottom_right_lon,
                      'top_left_lat': top_left_lat,
                      'top_left_lon': top_left_lon,
                      })


def resource_filter(request):
    if request.method == 'POST':
        form = ResourceFilterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            my_result = Resource.objects.filter(aspiration=cd['aspiration'],
                                                group=cd['group'],
                                                level=cd['level'],
                                                status=cd['status']
                                                )
            return render(request,
                          'lighthouseapp/result.html',
                          {'results': my_result})
        else:
            form = ResourceFilterForm()
            return render(request, 'lighthouseapp/filter.html', {'form': form})
    else:
        form = ResourceFilterForm()
        return render(request, 'lighthouseapp/filter.html', {'form': form})


def detail(request, pk):
    resource = Resource.objects.get(pk=pk)
    return render(request, 'lighthouseapp/detail.html', {'resource': resource})
