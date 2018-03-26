# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meat', '0002_auto_20180304_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_on_the_site_model',
            name='client',
            field=models.CharField(verbose_name='Кліент - ', default='', max_length=256),
        ),
    ]
