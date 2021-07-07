from django.db import models
from datetime import date
from model_utils import Choices

# Create your models here.

departments = (
    ('Dentistry', "Dentistry"),
    ('Cardiology', "Cardiology"),
    ('ENT Specialists', "ENT Specialists"),
    ('Psychiatry', 'Psychiatry'),
    ('Neuroanatomy', 'Neuroanatomy'),
    ('Blood Screening', 'Blood Screening'),
    ('Eye Care', 'Eye Care'),
    ('Physical Therapy', 'Physical Therapy'),
)


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    qualifications = models.CharField(max_length=100)
    department = models.CharField(choices=departments, max_length=100)
    image = models.ImageField(upload_to='images', null=True)

    def __str__(self):
        return self.name


class Appointments(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(choices=(('male', 'Male'),('female','Female')), max_length=10, default=None)
    age = models.IntegerField()
    phone = models.CharField(max_length=15)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)