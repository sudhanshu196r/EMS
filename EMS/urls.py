from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('addEmployee',addEmployee,name='addEmployee'),
    path('Employees',Employees,name='Employees'),
    path('deleteEmployee/<int:id>', deleteEmployee, name='deleteEmployee'),
    path('editEmployee/<int:id>', editEmployee, name='esitEmployee'),

]

app_name = 'EMS'
