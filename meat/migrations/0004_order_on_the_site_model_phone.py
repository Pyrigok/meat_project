# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meat', '0003_auto_20180323_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_on_the_site_model',
            name='phone',
            field=models.CharField(verbose_name='Номер телефону - ', default='', max_length=12),
        ),
    ]
