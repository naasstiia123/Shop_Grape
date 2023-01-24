from django.shortcuts import render

# Create your views here.
def condition_delivery(request):
    return render(request, 'context.html')

def condition_swap(request):
    return render(request, 'context1.html')
