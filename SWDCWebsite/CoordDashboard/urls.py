from django.urls import path

from . import views
urlpatterns = [
    path('dashboard', views.CoordDashboardView, name='CDashboard'),
    path('setpass', views.SetpasswordPageView, name='cresetpass'),
    path('Formfilling', views.FormFillingView, name='cFormFilling'),
    path('viewvolunteer', views.ApproveVolunteer, name='ApproveVolunteer'),
    path('rejectVolunteer', views.rejectVolunteerView, name='rejectVolunteer')

]
