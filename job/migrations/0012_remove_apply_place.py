# Generated by Django 4.2.23 on 2025-06-25 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0011_apply_place'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apply',
            name='place',
        ),
    ]
