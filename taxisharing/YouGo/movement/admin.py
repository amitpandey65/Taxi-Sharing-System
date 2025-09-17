
from django.contrib import admin
from .models import Trip

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
  list_display = ('employee_name', 'route', 'vehicle_number', 'shift_time')