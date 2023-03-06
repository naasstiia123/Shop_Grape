from django.shortcuts import render, get_object_or_404
import random
from .models import Product, Slider, Advantage, Offer, Gallery, Category_good, Type_good, Feedback
from cart.cart import Cart
from django.db.models import Q
from django.views.generic import ListView
from .forms import FeedbackForm

# Create your views here.
def main(request):
    """
    Shows the main page of the site.
    """
    products = Product.objects.filter(is_visible=True)
    slide = Slider.objects.filter(is_visible=True)
    advantage = Advantage.objects.filter(is_visible=True)
    offer = Offer.objects.filter(is_visible=True)
    gallery = Gallery.objects.filter(is_visible=True)
    cart = Cart(request)
    return render(request, 'main.html', context={'products': products,
                                                 'slide': slide,
                                                 'advantage': advantage,
                                                 'offer': offer,
                                                 'gallery': gallery,
                                                 'cart': cart})

def product(request, id, slug):
    """
    Shows the information about good.
    :param id: id of good which shows
    :param slug: slug of good which shows
    :return: page with details about good.
    """
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.product_id = id
            form.save()
            form.clean()
    form = FeedbackForm()
    products = get_object_or_404(Product, id=id, slug=slug, is_visible=True)
    feedback = Feedback.objects.filter(product_id=id, is_visible=True)
    return render(request, 'product.html', context={'product': products, 'form': form, 'feedback': feedback})

def menu_product(request, id):
    """
        Shows the list of goods in chosen category.
        :param id: id of category.
        :return: page with list of goods.
    """
    category = get_object_or_404(Category_good, id=id, is_visible=True)
    type = Type_good.objects.filter(is_visible=True, category=category.pk)
    product = Product.objects.filter(is_visible=True, category=category.pk)
    return render(request, 'product_menu.html', context={'type': type,
                                                         'product': product})

class Search(ListView):
    model = Product

    def get_queryset(self):
        """
        Search a special good by user.
        :return:list with goods which correspondence.
        """
        query = self.request.GET.get("q")
        query_title = query.title()
        object_list = Product.objects.filter(Q(name__icontains=query_title) | Q(slug__icontains=query) | Q(
            item__icontains=query) | Q(category__name__icontains=query_title)
            | Q(type__name__icontains=query_title))
        return object_list

