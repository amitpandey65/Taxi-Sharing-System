from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)

class FeedbackAdmin(admin.ModelAdmin):
  list_display = ('employee_name', 'comment', 'date')