# Generated by Django 3.2.4 on 2021-07-06 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appointmed', '0007_auto_20210706_2138'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DoctorAvailability',
        ),
        migrations.AlterField(
            model_name='doctor',
            name='department',
            field=models.CharField(choices=[('Dentistry', 'Dentistry'), ('Cardiology', 'Cardiology'), ('ENT Specialists', 'ENT Specialists'), ('Psychiatry', 'Psychiatry'), ('Neuroanatomy', 'Neuroanatomy'), ('Blood Screening', 'Blood Screening'), ('Eye Care', 'Eye Care'), ('Physical Therapy', 'Physical Therapy')], max_length=100),
        ),
    ]
