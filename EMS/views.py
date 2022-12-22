from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employee
from .forms import AddEmployeeForm
from .filters import EmpFilter
# Create your views here.

def home(request):
    #return HttpResponse('Hello World')
    count_all = Employee.objects.all().count()
    emp_on_leave = Employee.objects.filter(on_leave=True).count()
    active_emp = Employee.objects.filter(Active=True).count()
    context = {
        'count_all':count_all,
        'emp_on_leave':emp_on_leave,
        'active_emp':active_emp,
    }
    return render(request, 'home.html',context)

def addEmployee(request):
    if request.method=='POST':
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('EMS:Employees')

    elif request.method=='GET':
        form= AddEmployeeForm()
        context = {
            'form':form
        }
        return render(request,'addEmployee.html',context)



def Employees(request):
    emp = Employee.objects.all()

    myFilter = EmpFilter(request.GET,queryset=emp)
    emp=myFilter.qs
    details = {
        'allEmp' : emp.values(),'myFilter':myFilter
    }

    return render(request, 'Employees.html',details)

def deleteEmployee(request,id):
    emp_del = Employee.objects.get(Id=id)
    emp_del.delete()
    return redirect('/Employees')

def editEmployee(request,id):
    if request.method == 'POST':   
        emp_data= Employee.objects.get(Id=id)
        form = AddEmployeeForm(request.POST or None,instance=emp_data)
        if form.is_valid():
            on_leave = request.POST.get('on_leave')
            form.save(commit=False)
            if on_leave == True :
                form.Leave_count += 1
                form.save()
            return redirect('/Employees')

    elif request.method == 'GET':
        emp_data= Employee.objects.get(Id=id)
        form = AddEmployeeForm(instance=emp_data)
        context = {
            'form' : form
        }
        return render(request, 'editEmployee.html',context)
    
