"""
from .models import CustomerModel
from django import forms

class CustomerForm(forms.ModelForm):
	class Meta:
		model = CustomerModel
		fields = '__all__'
"""