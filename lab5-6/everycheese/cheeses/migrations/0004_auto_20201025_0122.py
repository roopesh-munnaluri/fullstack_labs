# Generated by Django 3.1.1 on 2020-10-25 01:22

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cheeses', '0003_cheese_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cheese',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='id', unique=True, verbose_name='Cheese Address'),
        ),
    ]
