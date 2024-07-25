from django.urls import path, include
from .view import *

urlpatterns = [
  path('api-list/', ProductsListApiView.as_view(),name='Api-List'), 
  path('api-detail/<pk>', ProductsDetailApiView.as_view(),name='Api-Detail'),  
]


