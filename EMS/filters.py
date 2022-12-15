import django_filters
from .models import *

class EmpFilter(django_filters.FilterSet):
    class Meta:
        model=Employee
        fields = [
            'Id','Name',
        ]