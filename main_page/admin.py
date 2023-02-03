from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'is_available', 'created', 'updated', 'is_visible', 'offer']
    list_filter = ['is_available', 'created', 'is_visible', 'updated']
    list_editable = ['price', 'is_available', 'is_visible', 'offer']

    prepopulated_fields = {'slug': ('name',)}

admin.site.register(models.Slider)

@admin.register(models.Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    list_display = ['desc', 'is_visible']
    list_editable = ['is_visible']

@admin.register(models.Category_good)
class Category_good(admin.ModelAdmin):
    list_display = ['name', 'is_visible']
    list_editable = ['is_visible']

@admin.register(models.Type_good)
class Type_good(admin.ModelAdmin):
    list_display = ['name', 'is_visible', 'category']
    list_editable = ['is_visible']

admin.site.register(models.Offer)
admin.site.register(models.Gallery)
admin.site.register(models.Phone)
admin.site.register(models.Email_adress)
admin.site.register(models.Address)

@admin.register(models.Feedback)
class Feedback(admin.ModelAdmin):
    list_display = ['date', 'name', 'product']
    list_filter = ['date', 'product']

