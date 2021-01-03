# Generated by Django 3.1.1 on 2020-10-25 01:30

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cheeses', '0004_auto_20201025_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cheese',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True, verbose_name='Cheese Address'),
        ),
    ]