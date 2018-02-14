from django.db import models

class RegistrationModel(models.Model):
	class Meta(object):
		verbose_name = u' - Зареєстровані клієнти'
		verbose_name_plural = u' - Зареєстровані клієнти'

	name = models.CharField (
		max_length = 30,
		blank = False,
		null = True,
		verbose_name = u"Ваше ім'я:")

	last_name = models.CharField(
		max_length = 30,
		blank = False,
		null = True,
		verbose_name = u'Ваше прізвище:')

	email = models.EmailField (
		max_length = 100,
		blank = False,
		null = False,
		verbose_name = u'Ваша email-адреса:')

	address = models.CharField (
		max_length = 256,
		blank = False,
		null = False,
		verbose_name = u'Ваша адреса:')

	phone = models.CharField(
		max_length = 10,
		blank = False, 
		null = False,
		verbose_name = u'Ваш телефон:')

	def __str__(self):
		return u'%s %s, %s' % (self.name, self.last_name, self.address)
