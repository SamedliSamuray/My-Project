from django.contrib import admin
from .models import *
from .forms import ColorForm

class ColorAdmin(admin.ModelAdmin):
    form = ColorForm
    list_display = ('clName', 'color_code')

admin.site.register(Color, ColorAdmin)
admin.site.register(Products_Categories)
admin.site.register(Brand)
admin.site.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('product', 'comment_name', 'comment_email', 'comment_content', 'created_at')
    search_fields = ('comment_name', 'comment_email', 'comment_content')

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name','brand', 'price', 'color', 'category','image','weight','dimension')

admin.site.register(Products, ProductsAdmin)