from django.shortcuts import render
import json
from cart.cart import Cart
from order.models import OrderItems
from order.forms import OrderForm
# Create your views here.

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        # form.save()
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItems.objects.create(order=order, product=item['product'], price=item['price'],
                                         quantity=item['quantity'])

            # clear the cart
            order.save()
            cart.clear()
            return render(request, 'order_created.html', {'order': order})
    else:
        form = OrderForm()
    return render(request, 'order_form.html', context={'cart': cart, 'form': form})
