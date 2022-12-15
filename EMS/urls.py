from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('addEmployee',addEmployee,name='addEmployee'),
    path('Employees',Employees,name='Employees'),
    path('deleteEmployee/<int:id>', deleteEmployee, name='deleteEmployee'),
    path('editEmployee/<int:id>', editEmployee, name='editEmployee'),
    #path('searchEmployee/<str:Name>',searchEmployee,name='searchEmployee')

]

app_name = 'EMS'
