from django import forms
from .models import Trip

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['employee_name', 'route', 'vehicle_number','shift_time']