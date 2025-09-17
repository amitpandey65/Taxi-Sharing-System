from django.shortcuts import render
from .models import Employee

def hr(request):
    employees = Employee.objects.all()
    return render(request, 'hr/employee.html', {'employees': employees})
