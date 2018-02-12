from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models import AssorthmentModel

def assorthment(request):
	assorthment = AssorthmentModel.objects.all()

	paginator = Paginator (assorthment, 6)
	page = request.GET.get ('page')

	try:
		assorthment = paginator.page(page)

	except PageNotAnInteger:
		assorthment = paginator.page(1)

	except EmptyPage:
		assorthment = paginator.page(paginator.num_page)

	return render (request, 'assorthment.html', {'assorthment': assorthment})