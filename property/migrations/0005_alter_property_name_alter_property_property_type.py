# Generated by Django 4.0.6 on 2022-08-01 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_alter_property_image_alter_property_property_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='name',
            field=models.CharField(max_length=50, verbose_name=' عنوان '),
        ),
        migrations.AlterField(
            model_name='property',
            name='property_type',
            field=models.CharField(choices=[('s', 'sale'), ('r', 'rate')], max_length=10),
        ),
    ]
