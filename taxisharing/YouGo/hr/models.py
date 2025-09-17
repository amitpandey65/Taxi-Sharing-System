from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    shift = models.CharField(max_length=50)

    def _str_(self):
        return self.name
