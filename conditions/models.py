from django.db import models

# Create your models here.
class Delivery(models.Model):
    order = models.TextField(max_length=700)
    deliv = models.TextField(max_length=700)
    pay = models.TextField(max_length=700)
    data = models.DateTimeField(auto_now=True)

class Swap(models.Model):
    desc = models.TextField(max_length=300)
    cond_swap_goods = models.TextField(max_length=700)
    cond_swap_money = models.TextField(max_length=700)

class Conditiont_swap(models.Model):
    cond = models.TextField(max_length=200)
