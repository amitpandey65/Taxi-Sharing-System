from django.db import models

class Vehicle(models.Model):
    number = models.CharField(max_length=20)
    model = models.CharField(max_length=50)
    driver_name = models.CharField(max_length=100)

    def _str_(self):
        return self.number
