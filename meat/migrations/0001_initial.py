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
            ],
            options={
                'verbose_name': ' - Списки замовлень',
                'verbose_name_plural': ' - Списки замовлень',
            },
        ),
        migrations.CreateModel(
            name='Registration_Model',
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
        migrations.CreateModel(
            name='RespondModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('text', models.ForeignKey(verbose_name='Кілька слів про продукт', max_length=256, to='meat.Registration_Model')),
            ],
            options={
                'verbose_name': 'Кілька слів про продукт',
                'verbose_name_plural': 'Кілька слів про продукт',
            },
        ),
        migrations.AddField(
            model_name='order_on_the_site_model',
            name='description',
            field=models.ForeignKey(verbose_name='Опис замовлення:', max_length=500, to='meat.Registration_Model'),
        ),
    ]
