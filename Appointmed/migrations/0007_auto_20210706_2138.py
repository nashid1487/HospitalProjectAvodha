# Generated by Django 3.2.4 on 2021-07-06 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appointmed', '0006_appointments_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorAvailability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available', models.CharField(max_length=10)),
                ('available_on', models.CharField(choices=[(0, 'monday'), (1, 'tuesday'), (2, 'wednesday'), (3, 'thursday'), (4, 'friday'), (5, 'saturday'), (6, 'sunday')], max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='available',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='slug',
        ),
    ]
