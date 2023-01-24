from django.contrib import admin
from .models import Order, OrderItems, City, Department, PayMethod
# Register your models here.


class OrderItemInline(admin.TabularInline):
    model = OrderItems
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'last_name', 'email', 'phone', 'city', 'department', 'paid', 'created',
                    'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]

class DepartmentInLine(admin.TabularInline):
    model = Department

@admin.register(City)
class City(admin.ModelAdmin):
    list_display = ['city', 'is_visible']
    list_editable = ['is_visible']

    inlines = [DepartmentInLine]

admin.site.register(PayMethod)
