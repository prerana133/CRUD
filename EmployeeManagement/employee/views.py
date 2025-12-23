from django.shortcuts import render,redirect,get_object_or_404
from .models import EmployeeModel
from . forms import EmployeeForm

# Create your views here.

def home(request):
    return render(request,'index.html')

def employee_details(request):
    employee = EmployeeModel.objects.all()
    return render(request,'employeedetails.html',{"employee":employee})

def add_emp(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('details')
    else:
        form = EmployeeForm()
        return render(request,'empform.html',{'form':form})
    
def update_emp(request,id):
        employee = get_object_or_404(EmployeeModel,id=id)
        if request.method == "POST":
            form = EmployeeForm(request.POST,instance=employee)
            if form.is_valid():
                form.save()
                return redirect('details')
        else:
            form = EmployeeForm(instance=employee)
            return render(request,'empform.html',{'form':form})
def delete(request,id):
    employee = get_object_or_404(EmployeeModel,id=id)
    employee.delete()
    return redirect('details') 