from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models import AssorthmentModel

def assorthment(request):
	assorthment = AssorthmentModel.objects.all()

	return render (request, 'assorthment.html', {'assorthment': assorthment})