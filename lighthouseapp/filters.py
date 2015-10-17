import django_filters
from .models import Resource

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Resource
        fields = ['category', 'aspiration', 'group', 'level']

        