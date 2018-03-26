# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meat', '0004_order_on_the_site_model_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_on_the_site_model',
            name='phone',
        ),
        migrations.AddField(
            model_name='order_on_the_site_model',
            name='tel',
            field=models.CharField(verbose_name='Номер телефону', default='', max_length=12),
        ),
        migrations.AlterField(
            model_name='order_on_the_site_model',
            name='client',
            field=models.CharField(verbose_name='Кліент', default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='order_on_the_site_model',
            name='created_on',
            field=models.DateField(verbose_name='Запис створений', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='order_on_the_site_model',
            name='description',
            field=models.CharField(verbose_name='Опис замовлення', max_length=500),
        ),
    ]
