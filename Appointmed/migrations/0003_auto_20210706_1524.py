# Generated by Django 3.2.4 on 2021-07-06 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appointmed', '0002_auto_20210705_2236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointments',
            name='dob',
        ),
        migrations.AddField(
            model_name='appointments',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default=None, max_length=10),
        ),
    ]
