# Generated by Django 4.0.6 on 2022-08-06 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_category_alter_property_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='property_type',
            field=models.CharField(choices=[('rate', 'rate'), ('sale', 'sale')], max_length=10),
        ),
    ]
