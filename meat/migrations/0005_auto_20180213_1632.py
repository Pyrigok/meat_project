# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meat', '0004_auto_20180213_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_on_the_site_model',
            name='description',
            field=models.CharField(verbose_name='Опис замовлення:', max_length=500),
        ),
        migrations.DeleteModel(
            name='RegistrationModel',
        ),
    ]
