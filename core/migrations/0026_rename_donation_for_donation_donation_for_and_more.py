# Generated by Django 4.2.3 on 2023-07-25 04:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_donation_donation_for_event_event_for_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donation',
            old_name='Donation_for',
            new_name='donation_for',
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2023, 7, 25, 9, 58, 53, 748404)),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 25, 9, 58, 53, 748404)),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 25, 9, 58, 53, 747403)),
        ),
    ]
