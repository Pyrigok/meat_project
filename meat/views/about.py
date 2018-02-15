from django.shortcuts import render
from ..models import RespondModel


def about(request):
	respond = RespondModel.objects.all()
	return render (request, 'about.html', {'respond': respond})