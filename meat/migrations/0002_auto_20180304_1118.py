# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_on_the_site_model',
            name='client',
            field=models.CharField(verbose_name='Кдіент - ', max_length=256, default=''),
        ),
    ]
