from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from ..models import RespondModel

@login_required
def add_respond(request):
	respond=RespondModel.objects.all()
	if request.method == 'POST':
		if request.POST.get('send_button') is not None:

			errors = {}
			data = {}

			text = request.POST.get ('text', '').strip()
			if not text:
				errors ['text'] = u"Коментар без добрих слів не відправляється!"
			else:
				data ['text'] = text

			if not errors:
				respond=RespondModel(**data)
				respond.save()

				return HttpResponseRedirect (u'%s?status_message=Відгук опубліковано!' %(reverse('add_respond')))

			else:
				return render (request, 'add_respond.html',
								{"errors": errors})

		elif request.POST.get ('cancel_button') is not None:
			return HttpResponseRedirect (u'%s?status_message=Написання відгука скасоване!' %(reverse('add_respond')))

	else:
		return render (request, 'add_respond.html', {'respond': respond})


@login_required
def show_respond(request):
	respond = RespondModel.objects.all()
	return render (request, 'about.html', {'respond': respond})