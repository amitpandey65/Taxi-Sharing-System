from django.db import models


class Manager(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    email = models.EmailField()

    def _str_(self):
        return self.name
