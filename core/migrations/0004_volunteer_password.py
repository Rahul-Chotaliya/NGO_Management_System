# Generated by Django 4.2.3 on 2023-07-19 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_staff_alter_volunteer_user_pic_delete_donor'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='password',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
