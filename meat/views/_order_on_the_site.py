from django.shortcuts import render
#from django.views.generic.edit import FormView
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.views.generic import CreateView
from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions

from ..models import Order_on_the_site_Model

class SendOrderForm(ModelForm):
	class Meta:
		model = Order_on_the_site_Model
		fields = ['name', 'email', 'address', 'phone', 'description', 'date']

	def __init__(self, *args, **kwargs):
		super(SendOrderForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper(self)

		self.helper.form_class = 'form-horisontal'
		self.helper.form_method = 'POST'
		self.helper.form_action = reverse ('_order_on_the_site')

		self.helper.help_text_inline = True
		self.helper.html5_required = True
		self.helper.label_class = 'col-sm-2 control-label'
		self.helper.field_class = 'col-sm-6 noborder'

		self.helper.add_input(
			Submit('send_button', u'Надіслати', css_class='btn btn-primary send_button'))
		self.helper.add_input(
			Submit('cancel_button', u'Скасувати', css_class='btn btn-link cancel_button'))

'''
	name = forms.CharField (
		label = u"Ваше ім'я:")

	email = forms.EmailField (
		label = u'Ваша email-адреса:')

	address = forms.CharField (
		label = u'Ваша адреса:')

	phone = forms.IntegerField(
		label = u'Ваш телефон:')

	description = forms.CharField(
		label = u'Опис замовлення:')'''

class SendOrderView(CreateView):
	model = Order_on_the_site_Model
	template_name = '_order_on_the_site.html'
	form_class = SendOrderForm

	'''name = form.cleaned_data['name']
		email = form.cleaned_data ['email']
		address = form.cleaned_data ['address']
		phone = form.cleaned_data ['phone']
		description = form.cleaned_data ['description']'''

	def get_success_url(self):
		return u'%s?status_message=Замовлення надіслане!' % reverse ('_order_on_the_site')

	def post(self,request, *args, **kwargs):
		if request.POST.get('cancel_button'):
			return HttpResponseRedirect(
				u'%s?status_message=Замовлення скасоване!' % reverse ('_order_on_the_site'))

		else:
			return super (SendOrderView, self).post(request, *args, **kwargs)


