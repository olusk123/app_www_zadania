# Generated by Django 5.1.3 on 2024-12-11 18:05

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_stanowisko_coach_osoba'),
    ]

    operations = [
        migrations.AlterField(
            model_name='osoba',
            name='data_dodania',
            field=models.DateField(default=app.models.get_current_date),
        ),
    ]
