# Generated by Django 5.0.2 on 2024-02-17 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_booking_delete_roomdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='services',
            field=models.ManyToManyField(related_name='services', to='rooms.roomservices'),
        ),
    ]