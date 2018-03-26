from django.contrib import admin
from django.contrib.auth import views as auth_views

from django.forms import ModelForm, ValidationError

from .models import Order_on_the_site_Model, AssorthmentModel, RespondModel
from django.core.urlresolvers import reverse

class OrderListAdmin(admin.ModelAdmin):
	list_display = ['client', 'phone', 'email', 'address', 'created_on', 'description']
	ordering = ['description']

class AssorthmentListAdmin(admin.ModelAdmin):
	list_display = ['product_name', 'product_description', 'product_price', 'remainder']
	ordering = ['product_name', 'product_price', 'remainder']

class RespondModelListAdmin(admin.ModelAdmin):
	list_display = ['author', 'text', 'created_on']

# Register your models here.
admin.site.register (Order_on_the_site_Model, OrderListAdmin)
admin.site.register (AssorthmentModel, AssorthmentListAdmin)
admin.site.register (RespondModel, RespondModelListAdmin)
