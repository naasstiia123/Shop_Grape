from django.urls import reverse
from django.db import models
from django.core.validators import RegexValidator
import uuid

# Create your models here.
class Category_good(models.Model):
    name = models.CharField(max_length=50, unique=True)
    is_visible = models.BooleanField(default=True)
    position = models.SmallIntegerField(unique=True)

    def __str__(self):
        return f'{self.name} {self.position}'

    class Meta:
        ordering = ('position',)

    def get_absolute_url(self):
        return reverse("main_page:menu", args=[self.id])

class Type_good(models.Model):
    name = models.CharField(max_length=50, unique=True)
    is_visible = models.BooleanField(default=True)
    position = models.SmallIntegerField(unique=True)
    category = models.ForeignKey(Category_good, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.position}'

    class Meta:
        ordering = ('position',)

class Slider(models.Model):
    photo = models.ImageField(upload_to='assets/slider/%Y%m')
    is_visible = models.BooleanField(default=True)

class Advantage(models.Model):
    desc = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='assets/advantage/%Y%m')
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.desc}'

class Offer(models.Model):
    offer = models.CharField(max_length=100, unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.offer}'

class Product(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    item = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(max_length=500)
    photo = models.ImageField(upload_to='assets/product/%Y%m')
    category = models.ForeignKey(Category_good, on_delete=models.CASCADE)
    type = models.ForeignKey(Type_good, on_delete=models.CASCADE, blank=True)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    is_visible = models.BooleanField(default=True)
    is_available = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return f'{self.name} {self.item}'

    def get_absolute_url(self):
        return reverse("main_page:product", args=[self.id, self.slug])


class Gallery(models.Model):
    photo = models.ImageField(upload_to='assets/gallery/%Y%m')
    is_visible = models.BooleanField(default=True)

class Phone(models.Model):
    phone_val = RegexValidator(regex=r'^\+?3?8?0\d{2}[- ]?(\d[- ]?){7}$', message='Не вірний формат номера')

    phone = models.CharField(max_length=16, validators=[phone_val])
    is_visible = models.BooleanField(default=True)
    is_viber = models.BooleanField(default=False)
    is_telegram = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.phone}'

class Email_adress(models.Model):
    email = models.EmailField()
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.email}'

class Address(models.Model):
    address = models.CharField(max_length=250)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.address}'

class Feedback(models.Model):
    name = models.CharField(max_length=50)
    message = models.TextField(max_length=300)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    is_visible = models.BooleanField(default=True)

    class Meta:
        ordering = ('date',)

    def __str__(self):
        return f'{self.date}, {self.name}: {self.message}'