from django.urls import path
from . import views

app_name = 'main_page'

urlpatterns = [
    path('', views.main, name='main'),
    path('<int:id>/<slug:slug>/', views.product, name='product'),
    path('<int:id>/', views.menu_product, name='menu'),
    path('search/', views.Search.as_view(template_name='search.html'), name='search_results'),
]
