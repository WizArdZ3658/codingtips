# Generated by Django 3.0.5 on 2020-06-20 15:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200620_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='dob',
            field=models.DateField(default=datetime.date(2020, 6, 20)),
        ),
    ]
