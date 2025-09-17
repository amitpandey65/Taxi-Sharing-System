from django.shortcuts import render
from .models import Feedback

def quality(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'quality/quality.html', {'feedbacks': feedbacks})
