from rest_framework.generics import ListAPIView, RetrieveAPIView
from ..models import Products
from .serializers import ProductSerializer

class ProductsListApiView(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    
class ProductsDetailApiView(RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'