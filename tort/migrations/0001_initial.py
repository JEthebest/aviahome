# Generated by Django 4.1.7 on 2023-03-16 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iata_code', models.CharField(blank=True, max_length=6, null=True, verbose_name='IATA код')),
                ('name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Имя')),
            ],
            options={
                'verbose_name': 'Аэрапорт',
                'verbose_name_plural': 'Аэропорта',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iata_code', models.CharField(blank=True, max_length=6, null=True, verbose_name='IATA код')),
                ('name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Имя')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
    ]
