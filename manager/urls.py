from django.urls import path
from . import views

app_name = 'manager'

urlpatterns = [
    path('orders/', views.orders_view, name='orders'),
    path('orders/update/<int:pk>', views.update_order, name='update_order'),
    path('orders/update_items/<int:pk>', views.update_order_items, name='update_order_items'),
    path('orders/del_items/<int:item>', views.del_order_items, name='del_order_items'),
    path('orders/change_quantity/<int:pk>', views.update_order_quantity, name='update_order_quantity'),
    path('orders/paid/<int:pk>', views.paid_order, name='paid_order'),
    path('feedback/', views.feedback_views, name='feedback'),
    path('feedback/update/<int:pk>', views.update_feedback, name='update_feedback'),
]
