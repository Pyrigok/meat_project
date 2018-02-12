from django.shortcuts import render

from ..models import RespondModel

def respond(request):
	respond = RespondModel.objects.all()

	return render (request, 'order_on_the_site.html', {'respond': respond})