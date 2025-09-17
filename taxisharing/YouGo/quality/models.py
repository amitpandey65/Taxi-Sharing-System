from django.db import models

class Feedback(models.Model):
    employee_name = models.CharField(max_length=100)
    comment = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.employee_name
