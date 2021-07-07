from django.urls import path
from . import views

app_name = 'Appointmed'

urlpatterns = [
    path('', views.DoctorList.as_view(), name='home'),
    path('appointment/', views.new_appointment, name='appointment')
]