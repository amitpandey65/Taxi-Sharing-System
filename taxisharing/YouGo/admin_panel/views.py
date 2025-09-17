from django.shortcuts import render
from .models import Manager

def admin_panel(request):
    managers = Manager.objects.all()
    return render(request, 'admin_panel/manager.html', {'managers': managers})
def home_view(request):
    return render(request, 'admin_panel/home.html')