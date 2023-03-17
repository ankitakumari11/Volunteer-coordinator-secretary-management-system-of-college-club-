from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.VDashboardView, name='vdashboard'),
    path('setpass', views.SetpasswordPageView, name='vresetpass'),
]
