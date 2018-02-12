from django.contrib import admin

from django.forms import ModelForm, ValidationError

from .models import Order_on_the_site_Model, AssorthmentModel, RegistrationModel, RespondModel
from django.core.urlresolvers import reverse

class OrderListAdmin(admin.ModelAdmin):
	list_display = ['description']
	ordering = ['description']

class AssorthmentListAdmin(admin.ModelAdmin):
	list_display = ['product_name', 'product_description', 'product_price', 'remainder']
	ordering = ['product_name', 'product_price', 'remainder']

# Register your models here.
admin.site.register (Order_on_the_site_Model, OrderListAdmin)
admin.site.register (AssorthmentModel, AssorthmentListAdmin)
admin.site.register (RegistrationModel)
admin.site.register (RespondModel)
