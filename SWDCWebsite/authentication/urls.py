from django.urls import path
from . import views
urlpatterns = [
    path('volunteer-registration', views.VolunteerRegistrationView, name='vreg'),
    path('coord-registration', views.CoordRegistrationView, name='creg'),
    path('sec-registration', views.SecRegistrationView, name='sreg'),
    path('login', views.LoginView, name='login'),
    path('logout', views.LogoutView, name='logout')
]


