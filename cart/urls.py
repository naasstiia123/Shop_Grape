from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add/<int:product_id>/', views.add_product, name='add_product'),
    path('remove/<int:product_id>/', views.remove_product, name='remove_product'),
    path('update/<int:product_id>/', views.update, name='update_quantity')
]