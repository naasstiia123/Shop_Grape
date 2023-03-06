from django import forms


QUANTITY = [(i, str(i)) for i in range(1, 11)]

class CartAddProduct(forms.Form):
    """
    Change quantity of goods
    """
    quantity = forms.TypedChoiceField(choices=QUANTITY,
                                      coerce=int)

