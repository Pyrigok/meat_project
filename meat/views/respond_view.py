from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from ..models import RespondModel

@login_required
def respond(request):
	if request.method == "POST":
		if request.POST.get('send_respond') is not None:

			errors = {}
			data = {}

			text = request.POST.get ('text', '').strip()
			if not text:
				errors ['text'] = u"Це поле є обов'язковим!"
			else:
				data ['text'] = text

			if not errors:
				respond_entry=RespondModel(*data)
				respond_entry.save()

				return HttpResponseRedirect (u'%s?status_message=Відгук опубліковано!' %(reverse('about')))

			else:
				return render (request, 'about.html', {"errors": errors})


	return render (request, 'about.html', {'respond': respond})