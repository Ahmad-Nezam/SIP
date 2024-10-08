# Generated by Django 5.0.6 on 2024-08-26 13:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0005_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteVilla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='group.user')),
                ('villa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='group.villas')),
            ],
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
