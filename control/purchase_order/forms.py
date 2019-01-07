import django
from django import forms
from django.forms import Textarea, TextInput

from control.purchase_order.models import PurchaseOrder


class PurchaseOrderForm(forms.ModelForm):

    class Meta:
        model = PurchaseOrder
        fields = ['vat', 'comments', 'supplier', 'currency', 'item']
        widgets = {
            'description': Textarea(attrs={'cols': 100, 'rows': 1}),
            'quantity': TextInput(attrs={'size': 7}),
            'unit_cost': TextInput(attrs={'size': 7}),
        }