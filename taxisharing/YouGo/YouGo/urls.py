from django.contrib import admin
from django.urls import path, include
from admin_panel import views as admin_views  # if using admin_panel
from django.contrib.auth import views as auth

urlpatterns = [
    path('', admin_views.home_view, name='home'),
    path('admin/', admin.site.urls),
    path('hr/', include('hr.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin_panel/', include('admin_panel.urls')),
    path('maintenance/', include('maintenance.urls')),
    path('movement/', include('movement.urls')),
    path('finance/', include('finance.urls')),
    path('quality/', include('quality.urls')),
]