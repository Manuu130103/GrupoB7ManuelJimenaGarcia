# Generated by Django 5.1.1 on 2024-10-03 09:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relecloud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cruise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(max_length=2000)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relecloud.destination')),
            ],
        ),
        migrations.CreateModel(
            name='InfoRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(max_length=2000)),
                ('cruise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relecloud.cruise')),
            ],
        ),
    ]
