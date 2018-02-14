from django.db import models

class RespondModel(models.Model):
	class Meta (object):
		verbose_name = u' - Відгуки'
		verbose_name_plural = u' - Відгуки'

	#text = models.ForeignKey('RegistrationModel',
	text = models.CharField(
		max_length = 256,
		blank = False,
		null = False,
		verbose_name = u'Кілька слів про продукт')

	def __str__(self):
		return (self.text)