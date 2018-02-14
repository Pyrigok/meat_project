# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meat', '0002_auto_20180204_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_on_the_site_model',
            name='description',
            field=models.CharField(verbose_name='Опис замовлення:', max_length=500),
        ),
        migrations.AlterField(
            model_name='respondmodel',
            name='text',
            field=models.CharField(verbose_name='Кілька слів про продукт', max_length=256),
        ),
        migrations.DeleteModel(
            name='RegistrationModel',
        ),
    ]
