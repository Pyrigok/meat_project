from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from ..models import RegistrationModel

def registration_view(request):

	if request.method == 'POST':
		if request.POST.get('send_button') is not None:

			errors = {}
			data = {}

			name = request.POST.get ('name', '').strip()
			if not name:
				errors ['name'] = u"Це поле є обов'язковим!"
			else:
				data ['name'] = name

			last_name = request.POST.get ('last_name', '').strip()
			if not last_name:
				errors ['last_name'] = u"Це поле є обов'язковим!"
			else:
				data ['last_name'] = last_name

			email = request.POST.get ('email', '').strip()
			if not email:
				errors ['email'] = u"Це поле є обов'язковим!"
			else:
				data ['email'] = email
				'''try:
					check=re.search(r'[\w.-]+@[w.]+, email')
				except Exception:
					errors ['email'] = u'Введіть коректну адресу електронної пошти!'
				else:'''


			address = request.POST.get ('address', '').strip()
			if not address:
				errors ['address'] = u"Це поле є обов'язковим!"
			else:
				data ['address'] = address

			phone = request.POST.get ('phone', '').strip()
			if not phone:
				errors ['phone'] = u"Це поле є обов'язковим!"
			else:
				data ['phone'] = phone

			if not errors:
				register_entry = RegistrationModel (**data)
				register_entry.save()

				return HttpResponseRedirect (
						u'%s?status_message=Ваші дані успішно збережено!' %(reverse('registration')))

			else:
				return render (request, 'registration.html',
						{'errors': errors})

		elif request.POST.get ('cancel_button') is not None:
			return HttpResponseRedirect (u'%s?status_message=Реєстрацію скасовано!' %reverse('home'))

	else:
		return render (request, 'registration.html', {})