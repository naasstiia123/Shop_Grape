from django.shortcuts import render, get_object_or_404
import random
from .models import Product, Slider, Advantage, Offer, Gallery, Category_good, Type_good, Feedback
from cart.cart import Cart
from django.db.models import Q
from django.views.generic import ListView
from .forms import FeedbackForm

# Create your views here.
def main(request):
    products = Product.objects.filter(is_visible=True)
    slide = Slider.objects.filter(is_visible=True)
    advantage = Advantage.objects.filter(is_visible=True)
    offer = Offer.objects.filter(is_visible=True)
    gallery = random.sample(list(Gallery.objects.filter(is_visible=True)), 6)
    cart = Cart(request)
    return render(request, 'main.html', context={'products': products,
                                                 'slide': slide,
                                                 'advantage': advantage,
                                                 'offer': offer,
                                                 'gallery': gallery,
                                                 'cart': cart})

def product(request, id, slug):
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
    category = get_object_or_404(Category_good, id=id, is_visible=True)
    type = Type_good.objects.filter(is_visible=True, category=category.pk)
    product = Product.objects.filter(is_visible=True, category=category.pk)
    return render(request, 'product_menu.html', context={'type': type,
                                                         'product': product})

class Search(ListView):

    def get_queryset(self):
        object_list = Product.objects.filter(Q(name__icontains=self.request.GET.get('q')) | Q(slug__icontains=self.request.GET.get('q')) | Q(
            item__icontains=self.request.GET.get('q')) | Q(category__name__icontains=self.request.GET.get('q')))
        return object_list

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = self.request.GET.get('q')
        return context
