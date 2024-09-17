"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home.views import *
from django.conf.urls import handler404
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', home_view,name="home"),
    path('about/', about_view,name="about"),
    path('blogs/', blogs_view,name="blogs"),
    path('products/', products_view,name="products"),
    path('products-details/<int:id>', product_details,name="products-details"),
    path('product-api/',include('home.api.urls')),
    path('checkout/',checkout_view, name='checkout'),
    path('shipping/',shipping_view, name='shipping'),
    path('payments/',payments_view, name='payments'),
    path('delete-order/<int:id>',delete_order, name='delete-order'),
    path('update-order/<int:id>',update_order, name='update-order'),
    path('apply-discount/',apply_discount, name='apply-discount'),
    path('delete-discount/',delete_discount, name='delete-discount'),
    path('address-add/',address_add, name='address-add'),
    path('delete-address/<int:id>',delete_address, name='delete-address'),
    path('update-address/<int:id>',update_address, name='update-address'),
    path('add-card/',add_card, name='add-card'),
    path('update-card/<int:id>',update_card, name='update-card'),
    path('order-summary/',order_summary_view, name='order-summary'),
    path('my-profil/',my_profil, name='my-profil'),
    path('update-user/',update_user, name='update-user'),
    path('my-settings/',my_settings, name='my-settings'),
    path('my-wishlist/',my_wishlist, name='my-wishlist'),
    path('add-wishlist/<int:id>',add_wishlist, name='add-wishlist'),
    path('remove-wishlist/<int:id>',remove_wishlist, name='remove-wishlist'),
    path('notifications/',notifications, name='notifications'),
    path('my-order/',my_order_view, name='my-order'),
    path('add-place/',add_place_order, name='add-place'),
    path('clear_filter_image_folder/',clear_filter_image_folder, name='clear_filter_image_folder'),
    path('manage-address/',manage_address_view, name='manage-address'),
    path('saved-cards/',saved_cards_view, name='saved-cards'),
    path('404/',custom_404, name='404'),
    path('account/',include('account.urls')),
    path("admin/", admin.site.urls),
]

# handler404 = 'home.views.custom_404'


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    