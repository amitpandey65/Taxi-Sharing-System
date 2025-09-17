from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import CustomUserRegistrationForm, CustomLoginForm

def registration_view(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserRegistrationForm()
    return render(request, 'accounts/registration.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home.html')  # Or your homepage
    else:
        form = CustomLoginForm()
    return render(request, 'accounts/login.html', {'form': form})
