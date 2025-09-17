from django.contrib import admin
from .models import Bill

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
   list_display = ('vendor', 'vehicle_number', 'amount')