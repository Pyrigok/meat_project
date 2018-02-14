from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from datetime import datetime
from django.contrib.auth.decorators import login_required

from ..models import Order_on_the_site_Model

@login_required
def order_on_the_site(request):
	if request.method == 'POST':
		if request.POST.get('send_button') is not None:

			errors = {}
			data = {}

			description = request.POST.get ('description', '').strip()
			if not description:
				errors ['description'] = u"Це поле є обов'язковим!"
			else:
				data ['description'] = description

			address = request.POST.get ('address', '').strip()
			if not description:
				errors ['address'] = u"Це поле є обов'язковим!"
			else:
				data ['address'] = address


			if not errors:
				order_entry = Order_on_the_site_Model (**data)
				order_entry.save()

				return HttpResponseRedirect (
						u'%s?status_message=Ваше замовлення успішно відправлено!' %(reverse('order_on_the_site')))

			else:
				return render (request, 'order_on_the_site.html',
						{'errors': errors})

		elif request.POST.get ('cancel_button') is not None:
			return HttpResponseRedirect (u'%s?status_message=Замовлення скасоване!' %reverse('home'))



	else:
		return render (request, 'order_on_the_site.html')