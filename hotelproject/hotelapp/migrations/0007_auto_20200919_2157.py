# Generated by Django 3.1.1 on 2020-09-19 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0006_bookingmodel_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookingmodel',
            name='status',
        ),
        migrations.AddField(
            model_name='roommodel',
            name='status',
            field=models.CharField(default='-', max_length=50),
        ),
    ]
