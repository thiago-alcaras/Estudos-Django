# Generated by Django 3.1.7 on 2021-03-19 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_recursos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recursos',
            name='recurso',
            field=models.CharField(max_length=100, verbose_name='Recurso'),
        ),
    ]