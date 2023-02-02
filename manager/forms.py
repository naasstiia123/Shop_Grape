from django import forms
from order.models import OrderItems
from main_page.models import Product

class UpdateOrderForm(forms.ModelForm):

    product = forms.ModelChoiceField(queryset=Product.objects.filter(is_visible=True, is_available=True))
    quantity = forms.IntegerField()

    class Meta:
        model = OrderItems
        fields = ['product', 'quantity', ]
