# Generated by Django 3.1.5 on 2021-02-06 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Attendance', '0002_logsfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='logsfile',
            name='total_members',
            field=models.CharField(default='Nill', max_length=20),
        ),
    ]
