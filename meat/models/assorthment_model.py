from django.db import models

class AssorthmentModel(models.Model):
	class Meta(object):
		verbose_name = u' - Асортимент продуктів'
		verbose_name_plural = u' - Асортимент продуктів'

	photo = models.ImageField(
		blank = False,
		null = False,
		verbose_name = u'Фото:')

	product_name = models.CharField(
		max_length = 15,
		blank = False,
		null = False,
		verbose_name = u'Назва:')

	product_description = models.CharField(
		max_length = 256,
		blank = False,
		null = False,
		verbose_name = u'Опис продукту:')

	unit = models.CharField(
		max_length = 10,
		blank = True,
		null = True,
		verbose_name = u'Одиниця виміру:')

	product_price = models.CharField(
		max_length = 10,
		blank = False,
		null = False,
		verbose_name = u'Ціна товару:'
		)

	remainder = models.CharField(
		max_length = 50,
		blank = True,
		null = True,
		verbose_name = u'Залишок на складі:')

	def __str__ (self):
		return u'%s, %s, %s' %(self.product_name, self.product_description, self.remainder)
