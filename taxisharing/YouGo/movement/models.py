from django.db import models

class Trip(models.Model):
    employee_name = models.CharField(max_length=100)
    route = models.CharField(max_length=100)
    vehicle_number = models.CharField(max_length=20)
    shift_time = models.CharField(max_length=50)

    def _str_(self):
        return f"{self.employee_name} - {self.route}"