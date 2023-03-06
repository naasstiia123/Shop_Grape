from django.shortcuts import render, redirect, get_object_or_404
from main_page.models import Product
from django.views.decorators.http import require_GET, require_POST
from .cart import Cart
from .forms import CartAddProduct
# Create your views here.

def cart(request):
    """
    Shows the information about user's cart.
    """
    cart = Cart(request)
    form = CartAddProduct()
    return render(request, 'cart.html', context={'cart': cart, 'form': form})


def add_product(request, product_id):
    """
    Add goods to user's cart.
    :param product_id:id of good which will be added

    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product, quantity=1, update_quantity=False)
    return redirect('cart:cart')

@require_POST
def update(request, product_id):
    """
    Change quantity of good.
    :param product_id:id of good which will be updated

    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProduct(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=True)
    return redirect('cart:cart')

def remove_product(request, product_id):
    """
    Remove the good from cart.
    :param product_id:id of good which will be removed

    """
    cart = Cart(request)
    product = get_object_or_404(Product,  id=product_id)
    cart.remove(product=product)
    return redirect('cart:cart')

