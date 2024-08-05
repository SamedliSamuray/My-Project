from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
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
    
    
class ProductImage(models.Model):
    product = models.ForeignKey(Products, related_name='images', on_delete=models.CASCADE)
    images = models.ImageField(upload_to='product_images/')
    
    def __str__(self):
        return f"Image for {self.product.name}"
    
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