# Generated by Django 5.1 on 2024-09-02 01:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pilots', '0002_alter_pilots_age'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pilots',
            new_name='Pilot',
        ),
    ]
