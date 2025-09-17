from django.shortcuts import render, redirect
from .forms import Trip

from .models import Trip

def movement(request):
    trips = Trip.objects.all()
    return render(request, 'movement/trip.html', {'trips': trips})
def add_trip(request):
    if request.method == 'POST':
        form = Trip(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movement_home')  # or wherever you want to go after submission
    else:
        form = Trip()
    return render(request, 'movement/add_trip.html', {'form':form})