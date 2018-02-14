# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meat', '0005_auto_20180213_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_on_the_site_model',
            name='address',
            field=models.CharField(verbose_name='Ваша адреса:', max_length=256, default=''),
        ),
    ]
