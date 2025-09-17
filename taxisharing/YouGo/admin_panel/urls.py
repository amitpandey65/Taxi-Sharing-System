from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('', views.admin_panel, name='admin_panel'),
]