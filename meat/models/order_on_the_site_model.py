from django.db import models

class Order_on_the_site_Model(models.Model):
	class Meta(object):
		verbose_name = u' - Списки замовлень'
		verbose_name_plural = u' - Списки замовлень'


	#description = models.ForeignKey('RegistrationModel',


	description = models.CharField (
		max_length = 500,
		blank = False,
		null = False,
		verbose_name = u'Опис замовлення:')

	address = models.CharField (
		max_length = 256,
		blank = False,
		null = False,
		default = '',
		verbose_name = u'Ваша адреса:')



	def __str__(self):
		return u'%s' % (self.description)