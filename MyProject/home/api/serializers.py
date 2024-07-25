from rest_framework import serializers
from ..models import *

class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.SerializerMethodField()
    color = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    price = serializers.IntegerField()
    weight = serializers.DecimalField(max_digits=10, decimal_places=2)
    width = serializers.DecimalField(max_digits=10, decimal_places=2)
    height = serializers.DecimalField(max_digits=10, decimal_places=2)
    depth = serializers.DecimalField(max_digits=10, decimal_places=2)
    instock = serializers.BooleanField()
    materials = serializers.CharField()

    class Meta:
        model = Products
        fields = [
            'id',
            'name',
            'brand',
            'price',
            'color',
            'category',
            'image',
            'descriptions',
            'weight',
            'width',
            'height',
            'depth',
            'instock',
            'materials'
        ]

    def get_brand(self, obj):
        return obj.brand.brand
    
    def get_color(self, obj):
        return {
            'name': obj.color.clName,
            'code': obj.color.color_code
        }
        
    def get_category(self, obj):
        return obj.category.name