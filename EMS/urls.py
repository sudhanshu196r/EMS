from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
]

app_name = 'EMS'
