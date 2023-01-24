from django.shortcuts import render, redirect, get_object_or_404
from main_page.models import Product
from django.views.decorators.http import require_GET
from .cart import Cart
# Create your views here.

def cart(request):
    cart = Cart(request)
    return render(request, 'cart.html', context={'cart': cart})

@require_GET
def add_product(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product, quantity=1, update_quantity=False)
    return redirect('cart:cart')

def remove_product(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product,  id=product_id)
    cart.remove(product=product)
    return redirect('cart:cart')

