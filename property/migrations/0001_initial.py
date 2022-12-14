# Generated by Django 4.0.6 on 2022-08-01 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('property_type', models.CharField(choices=[('r', 'rate'), ('s', 'sale')], max_length=10)),
                ('price', models.PositiveIntegerField()),
                ('area', models.DecimalField(decimal_places=2, max_digits=5)),
                ('beds_number', models.PositiveIntegerField()),
                ('baths_number', models.PositiveIntegerField()),
                ('garage_number', models.PositiveIntegerField()),
            ],
        ),
    ]
