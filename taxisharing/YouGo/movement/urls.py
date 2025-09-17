from django.urls import path
from . import views

urlpatterns = [
    path('', views.movement, name='movement'),
    # path('', views.movement_home, name='movement_home'),
    path('add/', views.add_trip, name='add_trip'),

]
