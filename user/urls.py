from django.urls import path

from . import views

urlpatterns = [
    path('userregistration/', views.UserRegistration.as_view(), name='User_Registration'),
]
