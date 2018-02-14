# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meat', '0006_order_on_the_site_model_address'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='respondmodel',
            options={'verbose_name': ' - Відгуки', 'verbose_name_plural': ' - Відгуки'},
        ),
    ]
