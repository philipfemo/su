# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-07 13:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='faculty',
            field=models.CharField(choices=[('HU', 'Humanistisk Fakultet'), ('JU', 'Juridisk Fakultet'), ('NV', 'Naturvidenskabelige Fakultet'), ('SAV', 'Samfundsvidenskabelige Fakultet'), ('SUV', 'Sundhedsvidenskabelige Fakultet'), ('TE', 'Teologiske Fakultet')], default='HU', max_length=3),
        ),
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='user',
            name='study',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]