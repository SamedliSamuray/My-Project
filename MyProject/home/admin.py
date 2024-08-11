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
class ProductImgAdmin(admin.TabularInline):
    model=ProductImage
    extra=1
class UserAddressAdmin(admin.ModelAdmin):
    list_display=('name','city','country')
admin.site.register(UserAddress,UserAddressAdmin)
class DiscountAdmin(admin.ModelAdmin):
    list_display=('code','is_active')
admin.site.register(Discounts,DiscountAdmin)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name','brand', 'price', 'color', 'category','weight','dimension')
    inlines = [ProductImgAdmin]
admin.site.register(Products, ProductsAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display=('product','customers')
admin.site.register(Order,OrderAdmin)

class OrderSummaryAdmin(admin.ModelAdmin):
    list_display=('user','grand_total')
admin.site.register(UserOrderSummary,OrderSummaryAdmin)

class PaymentsAdmin(admin.ModelAdmin):
    list_display=('user','transaction_id')
admin.site.register(Payments,PaymentsAdmin)
