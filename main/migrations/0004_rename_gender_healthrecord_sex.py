# Generated by Django 5.0.5 on 2024-06-01 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_healthrecord'),
    ]

    operations = [
        migrations.RenameField(
            model_name='healthrecord',
            old_name='gender',
            new_name='sex',
        ),
    ]
