from django.shortcuts import render,redirect , get_object_or_404
from .models import *
from django.db.models import Q , Avg
from .forms import *
# Create your views here.


def home_view(request):
    
    products_category = Products_Categories.objects.all()
    brands = Brand.objects.all()
    colors = Color.objects.all()
    products = Products.objects.all()
    
    categories = request.GET.getlist('category')
    products = Products.objects.all()
     
    
    if categories:
        products = Products.objects.filter(brand=categories.brand)
        
    context={'products_category':products_category,'brands':brands,"colors":colors,'products':products}
    return render(request,'home.html',context)

def product_details(request, id):
    product = get_object_or_404(Products, id=id)
    products = Products.objects.filter(name=product.name, brand=product.brand).exclude(color=product.color)
    related = Products.objects.filter(Q(brand=product.brand) | Q(materials=product.materials) | Q(category=product.category)).exclude(name=product.name)
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

    context = {
        'product': product,
        'colors': colors,
        'products': products,
        'related': related,
        'comments': comments,
        'average_rating': average_rating,
    }
    return render(request, 'product_details.html', context)


