from django.shortcuts import render
from ..models import RespondModel
from ..util import show_respond

def about(request):
	respond = RespondModel.objects.all()
	return render (request, 'about.html', {'respond': respond})