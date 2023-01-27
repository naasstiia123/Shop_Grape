from django.shortcuts import render
from .models import Swap, Conditiont_swap, Delivery

# Create your views here.
def condition_delivery(request):
    conditions = Delivery.objects.all()
    return render(request, 'context.html', context={'condition': conditions})

def condition_swap(request):
    swap = Swap.objects.all()
    conditions = Conditiont_swap.objects.all()
    return render(request, 'context1.html', context={'swap': swap,
                                                     'conditions': conditions})
