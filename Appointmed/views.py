from django.shortcuts import render, redirect
from django.views import generic
from .models import Doctor, Appointments, departments
from django import forms


# Create your views here.


class DoctorList(generic.ListView):
    queryset = Doctor.objects.filter().order_by('name')
    template_name = 'home.html'
    paginate_by = 9


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointments
        fields = ('name', 'gender', 'age', 'phone', 'doctor')



def new_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AppointmentForm()
    return render(request, 'appointment.html', {'form': form})
