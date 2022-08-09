# Generated by Django 4.0.6 on 2022-08-09 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_alter_property_property_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name=' عنوان ')),
                ('email', models.EmailField(max_length=254)),
                ('notes', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='property',
            name='property_type',
            field=models.CharField(choices=[('sale', 'sale'), ('rate', 'rate')], max_length=10),
        ),
    ]