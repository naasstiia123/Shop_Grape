from .cart import Cart

def cart(request):
    """
    Allow to show the information about cart in every template.
    :return:user's cart

    """
    return {'cart': Cart(request)}
