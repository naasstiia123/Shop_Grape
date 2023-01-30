from django import forms


QUANTITY = [(i, str(i)) for i in range(1, 11)]

class CartAddProduct(forms.Form):

    quantity = forms.TypedChoiceField(choices=QUANTITY,
                                      coerce=int)

