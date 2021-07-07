from django.contrib import admin
from .models import Doctor, Appointments


# Register your models here.


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'department')
    search_fields = ('name', 'department')


admin.site.register(Doctor, DoctorAdmin)


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'doctor', 'date')


admin.site.register(Appointments, AppointmentAdmin)
