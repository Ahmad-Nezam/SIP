# Generated by Django 5.0.6 on 2024-08-20 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0003_remove_booking_status_villas_location_villas_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='villas',
            name='price',
            field=models.IntegerField(default='150'),
            preserve_default=False,
        ),
    ]
