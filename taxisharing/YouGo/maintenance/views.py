from django.shortcuts import render
from .models import Vehicle

def maintenance(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'maintenance/vehicle.html', {'vehicles': vehicles})
