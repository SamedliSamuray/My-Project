from django.db import models
from django.db.models import Sum
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
# Create your models here.


class Products_Categories(models.Model):
    name=models.CharField(max_length=40)
    
    def __str__(self):
        return self.name
    
class Brand(models.Model):
    brand=models.CharField(max_length=40)
    
    def __str__(self):
        return self.brand
    
class Color(models.Model):
    clName=models.CharField(max_length=40)
    color_code = models.CharField(max_length=7, blank=True)
    
    def __str__(self):
        return self.clName

    
class Products(models.Model):
    
    name = models.CharField(max_length=60, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    price = models.BigIntegerField()
    color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Products_Categories, on_delete=models.CASCADE, related_name='products')
    descriptions=models.TextField( default=1  )
    weight = models.DecimalField( default=1.1 ,max_digits=5, decimal_places=2)
    width = models.DecimalField(default=1.1,max_digits=5, decimal_places=2) 
    height = models.DecimalField(default=1.1,max_digits=5, decimal_places=2) 
    depth = models.DecimalField(default=1.1,max_digits=5, decimal_places=2)
    instock = models.BooleanField(default=True)  
    materials = models.CharField(max_length=50, default='Wood')
    
    
    def __str__(self):
        return f"{self.brand} - {self.category} - {self.color} - {self.price}"
    
    def dimension(self):
        return f'{self.width} cm x {self.height} cm x {self.depth} cm'
    
    def get_main_image(self):
        first_image = self.images.first()
        return first_image.images.url if first_image else None

class Discounts(models.Model):
 
    code = models.CharField(max_length=50,unique=True)
    discount_type = models.CharField(max_length=50,choices=[('percentage', 'Percentage'), ('fixed', 'Fixed Amount')])
    discount_amount = models.DecimalField(max_digits=5, decimal_places=2)
    max_discount_amount = models.DecimalField(max_digits=5,decimal_places=2)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.code
class ProductImage(models.Model):
    product = models.ForeignKey(Products, related_name='images', on_delete=models.CASCADE)
    images = models.ImageField(upload_to='product_images/')
    
    def __str__(self):
        return f"Image for {self.product.name}"
class UserAddress(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='address') 
    name = models.CharField(max_length=50)  
    country=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    flat=models.CharField(max_length=50)
    Area=models.CharField(max_length=50)
    pin=models.CharField(max_length=50)
    phone=models.CharField(blank=True,null=True,default="", max_length=50)
    default_address = models.BooleanField(default=False)
    
    
    def __str__(self) -> str:
        return f'{self.name}-{self.pin}-{self.flat}-{self.Area}-{self.city} -{self.country}'
class Comment(models.Model):
    product = models.ForeignKey(Products,related_name='comments', on_delete=models.CASCADE)
    comment_name = models.CharField(max_length=50,verbose_name=_('Name:'))
    rating = models.IntegerField(
        verbose_name=_('Rating'),
        default=0,
        blank=True,
        choices=[(i, str(i)) for i in range(1, 6)], 
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comment_email = models.EmailField(verbose_name=_('E-mail:'))
    comment_content = models.TextField(verbose_name=_('Content:'))
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.comment_content[:20]
class Order(models.Model):
    product = models.ForeignKey(Products,related_name='order', on_delete=models.CASCADE)
    customers = models.ForeignKey(User,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    delivery = models.IntegerField(default=5,blank=True)
    discounts= models.ForeignKey(Discounts,null=True,db_constraint=False,on_delete=models.CASCADE,blank=True )
    def __str__(self):
        return self.product.name


class PaymentMethod(models.TextChoices):
    CREDIT_CARD = 'DC', 'Debit Card'
    PAYPAL = 'PP', 'PayPal'
    GOOGLE_PAY = 'GP', 'Google Pay'
    CASH_ON_DELIVERY = 'COD', 'Cash on Delivery'
class Payments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40,null=True,blank=True)
    payment_method = models.CharField(max_length=3, choices=PaymentMethod.choices)
    amount = models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    cvv = models.IntegerField(null=True,blank=True,validators=[MinValueValidator(100), MaxValueValidator(999)])
    payment_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Payment {self.transaction_id}"

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"

class UserOrderSummary(models.Model):    
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    discounts= models.ForeignKey(Discounts,null=True,db_constraint=False,on_delete=models.CASCADE,blank=True )
    discount_value= models.DecimalField(max_digits=10,decimal_places=2,default=0)
    subtotal= models.DecimalField(max_digits=10,decimal_places=2,default=0)
    payments = models.ForeignKey(Payments , null=True, blank=True,on_delete=models.CASCADE)
    address = models.ForeignKey(UserAddress, on_delete=models.SET_NULL, null=True, blank=True)
    total_delivery_cost= models.DecimalField(max_digits=10,decimal_places=2,default=0)
    grand_total= models.DecimalField(max_digits=10,decimal_places=2,default=0)
    def __str__(self):
        return self.user.username
    def get_orders_by_customer(self,customers):
        orders = Order.objects.filter(customers=customers, status=False).order_by('-date')
        subtotalPrice = orders.aggregate(total_subtotal=Sum('price'))['total_subtotal'] or 0
        total_weight = sum(order.product.weight * order.quantity for order in orders)
        self.total_delivery_cost = total_weight
        self.subtotal = subtotalPrice
        self.grand_total = subtotalPrice + self.total_delivery_cost
        
        self.save()


