from django.db import models
from django.core.validators import RegexValidator
from main_page.models import Product
from django.utils import timezone

# Create your models here.
class PayMethod(models.Model):
    method = models.CharField(max_length=100)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.method}'

class City(models.Model):
    city = models.CharField(max_length=50)
    is_visible = models.BooleanField(default=True)

    class Meta:
        ordering = ('city',)

    def __str__(self):
        return f'{self.city}'

class Department(models.Model):
    department = models.IntegerField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.TextField(max_length=300)
    is_visible = models.BooleanField(default=True)

    class Meta:
        ordering = ('department',)

    def __str__(self):
        return f'{self.city}, {self.address} Відділення № {self.department}'


class Order(models.Model):
    phone_val = RegexValidator(regex=r'^\+?3?8?0\d{2}[- ]?(\d[- ]?){7}$', message='Не вірний формат номера')

    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=16, validators=[phone_val])
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    pay_method = models.ForeignKey(PayMethod, on_delete=models.CASCADE)

    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} {self.last_name} {self.phone}'

    def get_total_cost(self):
        res = 0
        for item in self.items.all():
            res += item.get_coast()
        return res


class OrderItems(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f'{self.product}'

    def get_coast(self):
        return self.price * self.quantity
