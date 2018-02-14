# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meat', '0003_auto_20180213_1004'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name="Ваше ім'я:", max_length=30, null=True)),
                ('last_name', models.CharField(verbose_name='Ваше прізвище:', max_length=30, null=True)),
                ('email', models.EmailField(verbose_name='Ваша email-адреса:', max_length=100)),
                ('address', models.CharField(verbose_name='Ваша адреса:', max_length=256)),
                ('phone', models.CharField(verbose_name='Ваш телефон:', max_length=10)),
            ],
            options={
                'verbose_name': 'Зареєстровані клієнти',
                'verbose_name_plural': 'Зареєстровані клієнти',
            },
        ),
        migrations.AlterField(
            model_name='order_on_the_site_model',
            name='description',
            field=models.ForeignKey(verbose_name='Опис замовлення:', max_length=500, to='meat.RegistrationModel'),
        ),
    ]
