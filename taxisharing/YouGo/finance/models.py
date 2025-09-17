from django.db import models

class Bill(models.Model):
    vendor = models.CharField(max_length=100)
    vehicle_number = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def _str_(self):
        return f"{self.vendor} - ₹{self.amount}"
