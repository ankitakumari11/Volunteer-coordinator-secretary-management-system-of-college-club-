from django.urls import path
from . import views
urlpatterns = [
    path('dashboard', views.SecDashboardView, name='SDashboard'),
    path('setpass', views.SetpasswordPageView, name='sresetpass'),
    path('approve-coord', views.ApproveCoord, name='ApproveCoord'),
    path('rejectCoord', views.rejectCoordView, name='rejectCoord')

]
