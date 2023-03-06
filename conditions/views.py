from django.shortcuts import render
from .models import Swap, Conditiont_swap, Delivery, About

# Create your views here.
def condition_delivery(request):
    """
    Show the conditions of delivery.
    """
    conditions = Delivery.objects.filter(is_visible=True)
    return render(request, 'context.html', context={'condition': conditions})

def condition_swap(request):
    """
    Show conditions of swap goods.
    """
    swap = Swap.objects.filter(is_visible=True)
    conditions = Conditiont_swap.objects.filter(is_visible=True)
    return render(request, 'context1.html', context={'swap': swap,
                                                     'conditions': conditions})

def about(request):
    """
    Show the information about shop.
    """
    about = About.objects.filter(is_visible=True)
    return render(request, 'about.html', context={'about': about})
