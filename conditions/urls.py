from django.urls import path
from . import views

app_name = 'conditions'

urlpatterns = [
    path('delivery/', views.condition_delivery, name='delivery'),
    path('swap/', views.condition_swap, name='swap'),
]