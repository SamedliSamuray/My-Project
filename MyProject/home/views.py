from django.shortcuts import render,redirect , get_object_or_404
from .models import *
from django.db.models import Q , Avg , Count
from .forms import *
# Create your views here.


def products_view(request):
    
    products_category = Products_Categories.objects.annotate( items_count = Count('products') )
    brands = Brand.objects.annotate( items_count = Count('products') )
    colors = Color.objects.annotate( items_count = Count('products') )
    products = Products.objects.all().annotate(average_rating=Avg('comments__rating'))
    
    filter_category = request.GET.getlist('category')
    filter_brand = request.GET.getlist('brand')
    filter_color = request.GET.getlist('color')
    filter_price_min = request.GET.get('range-min')
    filter_price_max = request.GET.get('range-max')

    # if filter_category or filter_brand or filter_color or filter_price_min or filter_price_max:
    #     q = Q()
    #     if filter_category:
    #         q &= Q(category__in=filter_category)
    #     if filter_brand:
    #         q &= Q(brand__in=filter_brand)
    #     if filter_color:
    #         q &= Q(color__in=filter_color)
    #     if filter_price_min and filter_price_max:
    #         q &= Q(price__gte=filter_price_min) & Q(price__lte=filter_price_max)

    #     products = products.filter(q)
    
    context={'products_category':products_category,'brands':brands,"colors":colors,'products':products}
    return render(request,'products.html',context)

def product_details(request, id):
    product = get_object_or_404(Products, id=id)
    products = Products.objects.filter(name=product.name, brand=product.brand).exclude(color=product.color)
    related = Products.objects.filter(Q(brand=product.brand) | Q(materials=product.materials) | Q(category=product.category)).exclude(id=id)
    colors = Color.objects.all()
    comments = product.comments.all()
    average_rating = comments.aggregate(Avg('rating'))['rating__avg'] or 0

    if request.method == 'POST':
        comment_name = request.POST.get('comment_name')
        comment_content = request.POST.get('comment_content')
        rating = int(request.POST.get('rating'))

        new_comment = Comment(
            comment_name=comment_name,
            comment_content=comment_content,
            rating=rating,
            product=product
        )
        new_comment.save()

        return redirect('products-details', id=product.id)
    if request.method == 'GET':
        name = request.GET.get('name')
        name = request.GET.get('name')
        name = request.GET.get('name')
    context = {
        'product': product,
        'colors': colors,
        'products': products,
        'related': related,
        'comments': comments,
        'average_rating': average_rating,
    }
    return render(request, 'product_details.html', context)

def checkout_view(request):
    return render(request,'checkout.html')


