from django.db import models

# Create your models here.
class Delivery(models.Model):
    order = models.TextField(max_length=700)
    deliv = models.TextField(max_length=700)
    pay = models.TextField(max_length=700)
    data = models.DateTimeField(auto_now=True)
    is_visible = models.BooleanField(default=True)

class Swap(models.Model):
    desc = models.TextField(max_length=300)
    cond_swap_goods = models.TextField(max_length=700)
    cond_swap_money = models.TextField(max_length=700)
    is_visible = models.BooleanField(default=True)

class Conditiont_swap(models.Model):
    cond = models.TextField(max_length=200)
    is_visible = models.BooleanField(default=True)

class About(models.Model):
    about = models.TextField(max_length=1000)
    is_visible = models.BooleanField(default=True)
