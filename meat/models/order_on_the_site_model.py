from django.db import models

class Order_on_the_site_Model(models.Model):
	class Meta(object):
		verbose_name = u' - Списки замовлень'
		verbose_name_plural = u' - Списки замовлень'


	client = models.CharField(
		max_length = 256,
		blank = False,
		null = False,
		default = '',
		verbose_name = u'Кліент')

	phone = models.CharField(
		max_length = 10,
		blank = False,
		null = False,
		default = '',
		verbose_name = u'Номер телефону')

	email = models.CharField(
		max_length = 256,
		blank = False,
		null = False,
		default = '',
		verbose_name = u'Електронна пошта')

	description = models.CharField (
		max_length = 500,
		blank = False,
		null = False,
		verbose_name = u'Опис замовлення')

	address = models.CharField (
		max_length = 256,
		blank = False,
		null = False,
		default = '',
		verbose_name = u'Адреса:')

	created_on = models.DateField(auto_now_add=True,
		verbose_name = u'Запис створений')

	def __str__(self):
		return u'%s, %s, %s, %s, %s, %s' % (self.client, self.phone, self.email, self.description, self.created_on, self.address)