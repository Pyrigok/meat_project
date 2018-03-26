from django.shortcuts import render
from django.contrib.auth.models import User
from ..models import RespondModel
from django.http import HttpRequest


def about(request):
	respond = RespondModel.objects.all()
	
	return render (request, 'about.html', {'respond': respond})