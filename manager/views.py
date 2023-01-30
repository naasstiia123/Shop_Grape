from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from order.models import Order, OrderItems
from main_page.models import Feedback


# Create your views here.
def is_manager(user):
    return user.groups.filter(name='Managers').exists()

@login_required(login_url='/login/')
@user_passes_test(is_manager)
def orders_view(request):
    order = Order.objects.filter(is_processed=False)
    items = OrderItems.objects.all()
    items = OrderItems.objects.all()
    return render(request, 'orders_manager.html', context={'order': order, 'items': items})


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def feedback_views(request):
    feedback = Feedback.objects.filter(is_visible=True)
    return render(request, 'feedback_manager.html', context={'feedback': feedback})


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def update_order(request, pk):
    Order.objects.filter(pk=pk).update(is_processed=True)
    return redirect('manager:orders')

@login_required(login_url='/login/')
@user_passes_test(is_manager)
def paid_order(request, pk):
    Order.objects.filter(pk=pk).update(paid=True)
    return redirect('manager:orders')

@login_required(login_url='/login/')
@user_passes_test(is_manager)
def update_feedback(request, pk):
    Feedback.objects.filter(pk=pk).update(is_visible=False)
    return redirect('manager:feedback')



