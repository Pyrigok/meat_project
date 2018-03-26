# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssorthmentModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('photo', models.ImageField(verbose_name='Фото:', upload_to='')),
                ('product_name', models.CharField(verbose_name='Назва:', max_length=15)),
                ('product_description', models.CharField(verbose_name='Опис продукту:', max_length=256)),
                ('unit', models.CharField(verbose_name='Одиниця виміру:', max_length=10, blank=True, null=True)),
                ('product_price', models.CharField(verbose_name='Ціна товару:', max_length=10)),
                ('remainder', models.CharField(verbose_name='Залишок на складі:', max_length=50, blank=True, null=True)),
            ],
            options={
                'verbose_name': ' - Асортимент продуктів',
                'verbose_name_plural': ' - Асортимент продуктів',
            },
        ),
        migrations.CreateModel(
            name='Order_on_the_site_Model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('client', models.CharField(verbose_name='Автор - ', max_length=256, default='')),
                ('description', models.CharField(verbose_name='Опис замовлення:', max_length=500)),
                ('address', models.CharField(verbose_name='Адреса:', max_length=256, default='')),
                ('created_on', models.DateField(verbose_name='Запис створений - ', auto_now_add=True)),
            ],
            options={
                'verbose_name': ' - Списки замовлень',
                'verbose_name_plural': ' - Списки замовлень',
            },
        ),
        migrations.CreateModel(
            name='RespondModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('author', models.CharField(verbose_name='Автор - ', max_length=256, default='')),
                ('text', models.CharField(verbose_name='Кілька слів про продукт', max_length=256)),
                ('created_on', models.DateField(verbose_name='Запис створений - ', auto_now_add=True)),
            ],
            options={
                'verbose_name': ' - Відгуки клієнтів',
                'verbose_name_plural': ' - Відгуки',
            },
        ),
    ]
