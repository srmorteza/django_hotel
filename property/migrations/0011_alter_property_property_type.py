# Generated by Django 4.0.6 on 2022-08-10 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_alter_property_property_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='property_type',
            field=models.CharField(choices=[('sale', 'sale'), ('rate', 'rate')], max_length=10),
        ),
    ]