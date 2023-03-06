from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from order.models import Order, OrderItems
from main_page.models import Feedback
from .forms import UpdateOrderForm
from cart.forms import CartAddProduct
from django.views.decorators.http import require_POST


# Create your views here.
def is_manager(user):
    """
    Checking correspondence to manager's group.
    :param user: data about current identified user.
    :return:boolean result.
    """
    return user.groups.filter(name='Managers').exists()

@login_required(login_url='/login/')
@user_passes_test(is_manager)
def orders_view(request):
    """
    Shows page with customer's orders.
    """
    order = Order.objects.filter(is_processed=False)
    items = OrderItems.objects.all()
    form = UpdateOrderForm()
    form_quantity = CartAddProduct
    return render(request, 'orders_manager.html', context={'order': order, 'items': items, 'form': form,
                                                           'form_quantity': form_quantity})


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def feedback_views(request):
    """
    Shows page with customer's feedbacks.
    """
    feedback = Feedback.objects.filter(is_visible=True)
    return render(request, 'feedback_manager.html', context={'feedback': feedback})



@login_required(login_url='/login/')
@user_passes_test(is_manager)
def update_order(request, pk):
    """
    Change the status of order to processed.
    :param pk: id of order which will be updated.
    """
    Order.objects.filter(pk=pk).update(is_processed=True)
    return redirect('manager:orders')

@login_required(login_url='/login/')
@user_passes_test(is_manager)
def paid_order(request, pk):
    """
    Change the status of payment to paid.
    :param pk: id of order which will be updated.
    """
    Order.objects.filter(pk=pk).update(paid=True)
    return redirect('manager:orders')

@login_required(login_url='/login/')
@user_passes_test(is_manager)
def update_feedback(request, pk):
    """
    Hide the feedback from site.
    :param pk: id of feedback which will be hident.
    """
    Feedback.objects.filter(pk=pk).update(is_visible=False)
    return redirect('manager:feedback')


@require_POST
@login_required(login_url='/login/')
@user_passes_test(is_manager)
def update_order_items(request, pk):
    """
    Add goods to the order.
    :param pk:id of the good which will be added.
    """
    if request.method == 'POST':
        form = UpdateOrderForm(request.POST)
        form.save(commit=False)
        product = form.cleaned_data['product']
        if form.is_valid():
            OrderItems.objects.filter(order=pk).create(order_id=pk, product=product, price=product.price,
                                                quantity=form.cleaned_data[
                'quantity'])
    return redirect('manager:orders')

@require_POST
@login_required(login_url='/login/')
@user_passes_test(is_manager)
def update_order_quantity(request, pk):
    """
    Change quantity of the good in the order.
    :param pk:id of the good which will be changed.
    """
    if request.method == 'POST':
        form = CartAddProduct(request.POST)
        quantity = form.data['quantity']
        if form.is_valid():
            item = OrderItems.objects.filter(pk=pk)
            item.update(quantity=quantity)
    return redirect('manager:orders')

@login_required(login_url='/login/')
@user_passes_test(is_manager)
def del_order_items(request, item):
    """
    Remove a good from the order.
    :param pk:id of the good which will be removed.
    """
    OrderItems.objects.get(pk=item).delete()
    return redirect('manager:orders')



