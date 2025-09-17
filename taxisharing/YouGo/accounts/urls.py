from django.urls import path
from .views import login_view, registration_view
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', login_view, name='login'),
    path('registration/',registration_view, name='registration'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
