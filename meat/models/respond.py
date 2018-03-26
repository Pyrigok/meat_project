from django.db import models


class RespondModel(models.Model):
	class Meta (object):
		verbose_name = u' - Відгуки клієнтів'
		verbose_name_plural = u' - Відгуки'

	author = models.CharField(
		max_length = 256,
		blank = False,
		null = False,
		default = '',
		verbose_name = u'Автор - ')
	
	text = models.CharField(
		max_length = 256,
		blank = False,
		null = False,
		verbose_name = u'Кілька слів про продукт')

	created_on = models.DateField(auto_now_add=True,
		verbose_name = u'Запис створений - ')

	def __str__(self):
		return u'%s, %s, %s' %(self.author, self.text, self.created_on)