from django.shortcuts import render
from .models import Bill

def finance(request):
    bills = Bill.objects.all()
    return render(request, 'finance/bill.html', {'bills': bills})
