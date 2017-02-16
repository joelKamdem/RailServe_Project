# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 19:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance_on', models.DecimalField(decimal_places=4, max_digits=8, verbose_name='Distance covered while the device is active')),
                ('status', models.BooleanField(verbose_name='True if the device is on, and false otherwise')),
                ('speed', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Path',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.DecimalField(decimal_places=4, max_digits=10)),
                ('latitude', models.DecimalField(decimal_places=4, max_digits=10)),
            ],
        ),
        migrations.AddField(
            model_name='path',
            name='coord',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Railserve_tracking.Position'),
        ),
        migrations.AddField(
            model_name='path',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Railserve_tracking.Device'),
        ),
        migrations.AddField(
            model_name='device',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Railserve_tracking.Position'),
        ),
    ]