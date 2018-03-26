# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meat', '0005_auto_20180326_0945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_on_the_site_model',
            name='tel',
        ),
        migrations.AddField(
            model_name='order_on_the_site_model',
            name='email',
            field=models.CharField(default='', max_length=256, verbose_name='Електронна пошта'),
        ),
        migrations.AddField(
            model_name='order_on_the_site_model',
            name='phone',
            field=models.CharField(default='', max_length=10, verbose_name='Номер телефону'),
        ),
    ]
