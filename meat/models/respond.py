from django.db import models

class RespondModel(models.Model):
	class Meta (object):
		verbose_name = u'Кілька слів про продукт'
		verbose_name_plural = u'Кілька слів про продукт'

	text = models.ForeignKey('RegistrationModel',
		max_length = 256,
		blank = False,
		null = False,
		verbose_name = u'Кілька слів про продукт')

	def __str__(self):
		return (self.text)