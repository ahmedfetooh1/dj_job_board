import django_filters
from .models import JOB

class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = JOB
        fields = '__all__'
        exclude = ['image','published_at','salary','vacancy','slug','owner']
        