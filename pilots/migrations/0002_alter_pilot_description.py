# Generated by Django 5.1.2 on 2025-01-16 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pilots', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pilot',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
