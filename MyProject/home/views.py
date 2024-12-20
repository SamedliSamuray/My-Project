from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect , get_object_or_404
from .models import *
from account.models import *
from django.db.models import Q , Avg , Count
from .forms import *
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from urllib.parse import urlparse
from django.core.paginator import Paginator
from PIL import Image, ImageChops, ImageStat
from django.core.files.storage import FileSystemStorage
import os
import shutil
from core import settings
# Create your views here.

def home_view(request):
    user_order_summary = None 
    order = None
    order_count = 0
    wishlist = None
    wish_pro = None
    wish_count = 0
    if request.user.is_authenticated:
        user_order_summary, created = UserOrderSummary.objects.get_or_create(user=request.user)
        wishlist , created = MyWishList.objects.get_or_create(user=request.user)
        wish_pro = set(wishlist.products.values_list('id', flat=True))
        wish_count = len(wish_pro)
        user = ProfilPicture.objects.get_or_create(user=request.user)
        if created:
            user_order_summary.save()
        order = Order.objects.filter(customers=request.user, status=False)
        order_count = order.count()
    products = Products.objects.all().annotate(average_rating=Avg('comments__rating'))
    products =  products.annotate(review_count=Count('comments')).order_by('-average_rating')[:8]
    products_category = Products_Categories.objects.annotate( items_count = Count('products') )
    context = {'user_order_summary':user_order_summary,'order':order,'order_count':order_count,"products":products,'products_category':products_category,'wish_pro':wish_pro,
    'wish_count':wish_count}
    return render(request,'homepage.html',context)

def about_view(request):
    user_order_summary = None 
    order = None
    order_count = 0
    wishlist = None
    wish_pro = None
    wish_count = 0
    if request.user.is_authenticated:
        user_order_summary, created = UserOrderSummary.objects.get_or_create(user=request.user)
        
        wishlist , created = MyWishList.objects.get_or_create(user=request.user)
        wish_pro = set(wishlist.products.values_list('id', flat=True))
        wish_count = len(wish_pro)
        user = ProfilPicture.objects.get_or_create(user=request.user)
        if created:
            user_order_summary.save()
        order = Order.objects.filter(customers=request.user, status=False)
        order_count = order.count()
        if user_order_summary.discounts:
            user_order_summary.get_orders_discount(user_order_summary.discounts)
    context={
        'user_order_summary':user_order_summary,
        'order':order,
        'order_count':order_count,
        'wish_pro':wish_pro,
        'wish_count':wish_count
    }
    return render(request,'about.html',context)

def blogs_view(request):
    user_order_summary = None 
    order = None
    order_count = 0
    wishlist = None
    wish_pro = None
    wish_count = 0
    if request.user.is_authenticated:
        user_order_summary, created = UserOrderSummary.objects.get_or_create(user=request.user)
        wishlist , created = MyWishList.objects.get_or_create(user=request.user)
        wish_pro = set(wishlist.products.values_list('id', flat=True))
        wish_count = len(wish_pro)
        user = ProfilPicture.objects.get_or_create(user=request.user)
        if created:
            user_order_summary.save()
        order = Order.objects.filter(customers=request.user, status=False)
        order_count = order.count()
        if user_order_summary.discounts:
            user_order_summary.get_orders_discount(user_order_summary.discounts)
    context={
        'user_order_summary':user_order_summary,
        'order':order,
        'order_count':order_count,
        'wish_pro':wish_pro,
        'wish_count':wish_count
    }
    return render(request,'blogs.html',context)


def products_view(request):
    user_order_summary = None 
    order = None
    order_count = 0
    wishlist = None
    wish_pro = None
    wish_count = 0
    if request.user.is_authenticated:
        user_order_summary, created = UserOrderSummary.objects.get_or_create(user=request.user)
        order = Order.objects.filter(customers=request.user, status=False)
        order_count = order.count()
        wishlist = MyWishList.objects.get(user=request.user)
        wish_pro = set(wishlist.products.values_list('id', flat=True))
        wish_count = len(wish_pro)
    products_category = Products_Categories.objects.annotate( items_count = Count('products') ).order_by('name')
    brands = Brand.objects.annotate( items_count = Count('products') ).order_by('brand')
    colors = Color.objects.annotate( items_count = Count('products') ).order_by('clName')
    materials = ProductMaterials.objects.annotate( items_count = Count('products') ).order_by('material')
    products = Products.objects.all().annotate(average_rating=Avg('comments__rating'))
    products_count= len(Products.objects.all())
    
    
    filter_category = request.GET.getlist('category',[])
    filter_brand = request.GET.getlist('brand',[])
    filter_color = request.GET.getlist('color',[])
    filter_price_min = request.GET.get('range-min',0)
    filter_price_max = request.GET.get('range-max',7500)
    search = request.GET.get('search','')
    filter_sorter = request.GET.get('sorter','')
    filter_materials = request.GET.getlist('materials',[])    
    filter_upload_img = None
    
    if request.method == 'POST':
        if 'upload_img' in request.FILES:
            filter_upload_img = request.FILES['upload_img']
            if filter_upload_img:
                fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'filter_image'))
                filename = fs.save(filter_upload_img.name, filter_upload_img)
                
                uploaded_image_url = os.path.join(settings.MEDIA_URL, 'filter_image', filename)

                products = find_similar_products(filter_upload_img, products)
                filter_upload_img = uploaded_image_url
        
    
    if filter_category or filter_brand or filter_color or filter_price_min or filter_price_max or search or filter_sorter or filter_materials:
        if filter_category:
            products = products.filter(category__in=filter_category)
        if filter_brand:
            products = products.filter(brand__in=filter_brand)
        if filter_color:
            products = products.filter(color__in=filter_color)
        if filter_price_min and filter_price_max:
            products = products.filter(price__gte=filter_price_min, price__lte=filter_price_max)
        if filter_materials:
            products = products.filter(material__in=filter_materials)
        if search:
            products = products.filter(
            Q(brand__brand__icontains=search) | Q(color__clName__icontains=search) | Q(category__name__icontains=search) | Q(name__icontains=search)) 
        if filter_sorter:
            if filter_sorter == 'Price Low-High':
                products = products.order_by('price')
            elif filter_sorter == 'Price High-Low':
                products = products.order_by('-price')
            elif filter_sorter == 'Bestseller':
                products =  products.annotate(review_count=Count('comments')).order_by('-average_rating')
            elif filter_sorter == 'Reviews Count':
                products = products.annotate(review_count=Count('comments')).order_by('-review_count')
        

    params = request.GET.copy()
    if 'page' in params:
        params.pop('page')
     
    paginator = Paginator(products, 12)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    
    context={'user_order_summary':user_order_summary,'products_count':products_count,'order':order,'order_count':order_count,'products_category':products_category,'brands':brands,"colors":colors,'materials':materials,'products':page_obj,'filter_price_min':filter_price_min,'filter_price_max':filter_price_max,'filter_category':filter_category,'filter_brand':filter_brand,'filter_color':filter_color,'filter_materials':filter_materials,'search':search,'filter_sorter':filter_sorter,'filter_upload_img':filter_upload_img,'params':params,'wish_pro':wish_pro,'wish_count':wish_count}
    
    return render(request,'products.html',context)

    
def product_details(request, id):
    product = get_object_or_404(Products, id=id)
    products = Products.objects.filter(name=product.name, brand=product.brand).exclude(color=product.color)
    product_materials = set(product.material.values_list('id', flat=True))
    related = Products.objects.filter(Q(brand=product.brand) | Q(material__in=product_materials) | Q(category=product.category)).exclude(id=id).distinct()
    colors = Color.objects.all()
    user_order_summary = None 
    orders = None
    order_count = 0
    wishlist = None
    wish_pro = None
    wish_count =0
    
    if request.user.is_authenticated:
        user_order_summary, created = UserOrderSummary.objects.get_or_create(user=request.user)
        orders = Order.objects.filter(customers=request.user, status=False)
        order_count = orders.count()
        wishlist = MyWishList.objects.get(user=request.user)
        wish_pro = set(wishlist.products.values_list('id', flat=True))
        wish_count = len(wish_pro)
    comments = product.comments.all()
    average_rating = comments.aggregate(Avg('rating'))['rating__avg'] or 0
    profil_image =''
    if request.user.is_authenticated:
        user_profile = ProfilPicture.objects.get(user=request.user)
        profil_image = user_profile.image
    else:
        profil_image = '/profil_picture/unnamed.jpg'
    if request.method == 'POST':
       if 'comment_name' in request.POST:
            comment_content = request.POST.get('comment_content')
            rating = int(request.POST.get('rating'))
            
            comment_name = request.POST.get('comment_name')

            new_comment = Comment(
            comment_name=comment_name,
            image=profil_image,
            comment_content=comment_content,
            rating=rating,
            product=product
            )
            new_comment.save()
            messages.success(request,'Your review has been added successfully.')
            
            return redirect('products-details', id=product.id)
       elif 'product_id' in request.POST:
            product_id = request.POST.get('product_id')
            quantity = int(request.POST.get('quantity'))
            
            product = get_object_or_404(Products, id=product_id)
            have_order = Order.objects.filter(product_id=product_id,customers=request.user).first()
            if have_order:
                have_order.quantity+=quantity
                have_order.price=have_order.quantity*have_order.price
                have_order.save()
            else:
                order = Order(
                    product=product,
                    customers=request.user,
                    quantity=quantity,
                    price=product.price * quantity
                )
                order.save()
                user_order_summary = UserOrderSummary.objects.get_or_create(user=request.user)
                user_order = UserOrderSummary.objects.get(user=request.user)
                user_order.get_orders_by_customer(request.user)
                user_order.save()
                

                
            return redirect('products-details', id=product.id)

    context = {
        'wish_pro':wish_pro,
        'order':orders,
        'user_order_summary':user_order_summary,
        'order_count':order_count,
        'product': product,
        'colors': colors,
        'products': products,
        'related': related,
        'comments': comments,
        'average_rating': average_rating,
        'wish_count':wish_count,
        'profil_image':profil_image
    }
    return render(request, 'product_details.html', context)

def delete_order(request,id):
    order = get_object_or_404(Order,id=id)
    order.delete() 
    user_order_summary, created = UserOrderSummary.objects.get_or_create(user=request.user)
    user_order_summary.get_orders_by_customer(request.user)
    if user_order_summary.discounts:
       user_order_summary.get_orders_discount(user_order_summary.discounts)
    
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def update_order(request,id):
    order = get_object_or_404(Order,id=id)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action=='increment':
            order.quantity =order.quantity+ 1
        elif action == 'decrement' and order.quantity > 1:
            order.quantity = order.quantity-1
    
        order.price = order.quantity * order.product.price
        order.save()
        user_order_summary, created = UserOrderSummary.objects.get_or_create(user=request.user)
        user_order_summary.get_orders_by_customer(request.user)
        if user_order_summary.discounts:
           user_order_summary.get_orders_discount(user_order_summary.discounts)
        user_order_summary.save()
        
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))    


@login_required(login_url='account:login')
def checkout_view(request):
   
    order = Order.objects.filter(customers=request.user, status=False)
    order_count = order.count()
    user_order_summary, created = UserOrderSummary.objects.get_or_create(user=request.user)
    user_order_summary.get_orders_by_customer(request.user)
    wishlist = MyWishList.objects.get(user=request.user)
    wish_pro = set(wishlist.products.values_list('id', flat=True))
    wish_count = len(wish_pro)
    if user_order_summary.discounts:
        user_order_summary.get_orders_discount(user_order_summary.discounts)
      
    context={
        'user_order_summary':user_order_summary,
        'order':order,
        'order_count':order_count,
        'wish_pro':wish_pro,
        'wish_count':wish_count
    }
    return render(request,'checkout.html',context)

@login_required(login_url='account:login')
def shipping_view(request):
    order = Order.objects.filter(customers=request.user, status=False)
    order_count = order.count()
    user_order_summary, created = UserOrderSummary.objects.get_or_create(user=request.user)
    address = UserAddress.objects.filter(user=request.user)
    wishlist = MyWishList.objects.get(user=request.user)
    wish_pro = set(wishlist.products.values_list('id', flat=True))
    wish_count = len(wish_pro)
    if request.method == 'POST':
        id=request.POST.get('default_adress')
        default_address = UserAddress.objects.get(id=id)
        user_order_summary.address = default_address
        user_order_summary.save()
        return redirect('payments')
    context={'address':address,'user_order_summary':user_order_summary,'order':order,'order_count':order_count,'wish_pro':wish_pro,'wish_count':wish_count}
    return render(request,'shipping.html',context)

def apply_discount(request):
    order = Order.objects.filter(customers=request.user, status=False)
    user_order_summary, created = UserOrderSummary.objects.get_or_create(user=request.user)
    user_order_summary.get_orders_by_customer(request.user)
    discount_code = request.POST.get('discount_code')
    messages
    user_order_summary.discount_value=0.00
    discount_value = 0
    discount=discount_code
    if discount_code and user_order_summary.subtotal>0: 
        try:
            discount= Discounts.objects.get(code=discount_code,is_active=True)
            user_order_summary.get_orders_discount(discount_code)
            discount_value = user_order_summary.discount_value
            for ord in order:
                ord.discounts=discount
                ord.save()
            
            messages.success(request, f'{discount_code} code successfully redeemed, discount ${user_order_summary.discount_value}.')
        except Discounts.DoesNotExist:
            messages.warning(request,f'"{discount_code}" code is invalid')
    elif not discount_code and user_order_summary.subtotal>0:
        
        messages.warning(request, 'You have not entered a discount code.')
    else:
        messages.warning(request, 'There are currently no items in your cart..')
        
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def delete_discount(request):
    
    user_order_summary, created = UserOrderSummary.objects.get_or_create(user=request.user)
    user_order_summary.discounts = None
    user_order_summary.discount_value = 0
    user_order_summary.get_orders_by_customer(request.user)
    user_order_summary.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def address_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        flat = request.POST.get('flat')
        area = request.POST.get('area')
        city = request.POST.get('city')
        pin_code = request.POST.get('pin-code')
        state = request.POST.get('state')
        default_address = request.POST.get('default-address') is not None
        
        address = UserAddress.objects.create(user=request.user,name=name,phone=phone,flat=flat,country=state,city=city,Area=area,pin=pin_code,default_address=default_address)
        address.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def delete_address(request,id):
    address = UserAddress.objects.get(id=id)
    address.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def update_address(request,id):
    order = Order.objects.filter(customers=request.user, status=False)
    order_count = order.count()
    user_order_summary, created = UserOrderSummary.objects.get_or_create(user=request.user)
    address = UserAddress.objects.filter(user=request.user)
    update_address = get_object_or_404(UserAddress, id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        flat = request.POST.get('flat')
        area = request.POST.get('area')
        city = request.POST.get('city')
        pin_code = request.POST.get('pin-code')
        state = request.POST.get('state')
        default_address = request.POST.get('default-address') is not None
        
        update_address.name = name
        update_address.phone = phone
        update_address.flat = flat
        update_address.Area = area
        update_address.city = city
        update_address.pin = pin_code
        update_address.country = state
        update_address.default_address = default_address
        update_address.save()
        return redirect('shipping')
    context={'address':address,'user_order_summary':user_order_summary,'update_address': update_address,'order':order,'order_count':order_count}
    return render(request, 'shipping.html',context)

@login_required(login_url='account:login')    
def payments_view(request):
    order = Order.objects.filter(customers=request.user, status=False)
    order_count = order.count()
    user_order_summary, created = UserOrderSummary.objects.get_or_create(user=request.user)
    address = UserAddress.objects.filter(user=request.user)
    wishlist = MyWishList.objects.get(user=request.user)
    wish_pro = set(wishlist.products.values_list('id', flat=True))
    wish_count = len(wish_pro)
    context={'address':address,'user_order_summary':user_order_summary,'update_address': update_address,'order':order,'order_count':order_count,'wish_pro':wish_pro,
    'wish_count':wish_count}
    return render(request, 'payment.html',context)

def add_card(request):
    user_order_summary = UserOrderSummary.objects.filter(user=request.user).first()
    if request.method == "POST":
        payment_method = request.POST.get('method')
        amount = user_order_summary.grand_total
        name = request.POST.get('name')
        if payment_method != 'COD':
            transaction_id = request.POST.get('transaction_id')
            cvv = request.POST.get('cvv')
            payment_date=request.POST.get('payment_date')
            paymants_card =Payments.objects.create(
                user=request.user,
                name=name,
                payment_method=payment_method,
                transaction_id=transaction_id,
                payment_date=payment_date,
                cvv=cvv,amount=amount)
            messages.success(request,'Payment information has been added successfully . . .')
            
        else:
            paymants_card = Payments.objects.create(user=request.user,name=name,payment_method=payment_method,amount=amount)
        paymants_card.save()
        user_order_summary.payments = paymants_card
        user_order_summary.save()
    return redirect('payments')

def update_card(request ,id):
    user_order_summary = UserOrderSummary.objects.get(user=request.user)
    
    card = Payments.objects.filter(user=request.user)
    upd_card = get_object_or_404(Payments, id=id)
    if request.method == 'POST':
        payment_method = request.POST.get('method')
        name = request.POST.get('name')
        
        if payment_method != 'COD':
            transaction_id = request.POST.get('transaction_id')
            cvv = request.POST.get('cvv')
            payment_date=request.POST.get('payment_date')
        
        upd_card.payment_method = payment_method
        upd_card.name = name
        upd_card.amount = user_order_summary.grand_total
        if payment_method != 'COD':
            upd_card.transaction_id = transaction_id
            upd_card.cvv = cvv
            upd_card.payment_date = payment_date
        upd_card.save()
            
        messages.success(request,'Payment information has been added successfully . . .')
        return redirect('payments')
    
    context={'user_order_summary':user_order_summary,'card': card,'upd_card':upd_card,'user_order_summary':user_order_summary}
    return render(request, 'payment.html',context)

def order_summary_view(request):
    order = Order.objects.filter(customers = request.user)
    order_count = order.count()
    user_order_summary, created = UserOrderSummary.objects.get_or_create(user=request.user)
    wishlist = MyWishList.objects.get(user=request.user)
    wish_pro = set(wishlist.products.values_list('id', flat=True))
    wish_count = len(wish_pro)
    context ={'order':order,'user_order_summary':user_order_summary,'order_count':order_count,'wish_pro':wish_pro,'wish_count':wish_count}
    if not user_order_summary.payments.transaction_id :
        messages.warning(request,'Please add your payment information . . .')
        return redirect('payments')
    return render(request,'orderSummary.html',context)

@login_required(login_url='account:login')
def my_order_view(request):
    order = Order.objects.filter(customers = request.user)
    order_count = order.count()
    place_order = OrdersPlace.objects.filter(customers = request.user).order_by('-date')
    user_order_summary, created = UserOrderSummary.objects.get_or_create(user=request.user)
    wishlist = MyWishList.objects.get(user=request.user)
    wish_pro = set(wishlist.products.values_list('id', flat=True))
    wish_count = len(wish_pro)
    search_place = request.GET.get('search_place','')  
    if request.method == 'GET':
        if search_place:
            place_order = place_order.filter( 
            Q(product__brand__brand__icontains = search_place) | Q(product__color__clName__icontains = search_place) | Q(product__category__name__icontains = search_place) | Q(product__name__icontains = search_place)
            )
    context = {
    'order':order,
    'user_order_summary':user_order_summary,
    'order_count':order_count,
    'wish_pro':wish_pro,
    'wish_count':wish_count,
    'place_order':place_order,
    'search_place':search_place,
    } 
    
    return render(request,'myOrders.html',context)



def calculate_rms_difference(image1, image2):
    
    diff = ImageChops.difference(image1, image2)
    stat = ImageStat.Stat(diff)
    return sum(stat.mean)

def find_similar_products(filter_upload_img, products):
    filter_upload_img = Image.open(filter_upload_img).convert('RGB')
    similarities = []

    for product in products:
        min_rms = float('inf')
        
        for image_ins in product.images.all():
            product_img = Image.open(image_ins.images.path).convert('RGB')
            rms = calculate_rms_difference(filter_upload_img, product_img)
            min_rms = min(min_rms, rms)
        
        
        if min_rms < 50:
            similarities.append((min_rms, product))
    
    
    similarities.sort(key=lambda x: x[0])
    
    
    return [product for rms, product in similarities]


def custom_404(request):
    return render(request, '404.html')

def clear_filter_image_folder(request):
    filter_image_folder = os.path.join(settings.MEDIA_ROOT, 'filter_image')
    
    if os.path.exists(filter_image_folder):
    
        for filename in os.listdir(filter_image_folder):
            file_path = os.path.join(filter_image_folder, filename)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)  
            elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                    
    return redirect('products')

@login_required(login_url='account:login')
def my_wishlist(request):
    order = Order.objects.filter(customers=request.user, status=False)
    order_count = order.count()
    user_order_summary, created = UserOrderSummary.objects.get_or_create(user=request.user)
    user_order_summary.get_orders_by_customer(request.user)
    wishlist = MyWishList.objects.get(user=request.user)
    wish_pro = set(wishlist.products.values_list('id', flat=True))
    products = wishlist.products.all()
    wish_count = len(wish_pro)
    if user_order_summary.discounts:
        user_order_summary.get_orders_discount(user_order_summary.discounts)
      
    context={
        'user_order_summary':user_order_summary,
        'order':order,
        'order_count':order_count,
        'wish_pro':wish_pro,
        'wish_count':wish_count,
        'products':products,
    }
    return render(request,'My_wishlist.html',context)

def add_wishlist(request,id):
    product = get_object_or_404(Products, id=id)
    wishlist, created = MyWishList.objects.get_or_create(user=request.user)
    wishlist.products.add(product)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def remove_wishlist(request,id):
    product = get_object_or_404(Products, id=id)
    wishlist, created = MyWishList.objects.get_or_create(user=request.user)
    wishlist.products.remove(product)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='account:login')
def my_profil(request):
    order = Order.objects.filter(customers=request.user, status=False)
    order_count = order.count()
    user_order_summary, created = UserOrderSummary.objects.get_or_create(user=request.user)
    user_order_summary.get_orders_by_customer(request.user)
    notifications = UserNotifications.objects.filter(user = request.user)
    wishlist = MyWishList.objects.get(user=request.user)
    wish_pro = set(wishlist.products.values_list('id', flat=True))
    wish_count = len(wish_pro)
    if user_order_summary.discounts:
        user_order_summary.get_orders_discount(user_order_summary.discounts)
    if request.method == 'POST':
        profile_image = request.FILES.get('profil_img')
        user_profile = ProfilPicture.objects.get(user=request.user)
        
        if profile_image:
            user_profile.image = profile_image  
            user_profile.save()  
            notifications = UserNotifications(
            user = request.user,
            method = NotificationsMethod.ProfilImage
            )
            notifications.save()
        
        return redirect('my-profil') 
    context={
        'notifications':notifications,
        'user_order_summary':user_order_summary,
        'order':order,
        'order_count':order_count,
        'wish_pro':wish_pro,
        'wish_count':wish_count
    }
    return render(request,'My_profile.html',context)

def update_user(request):
    user = request.user
    userProfil, created = ProfilPicture.objects.get_or_create(user=request.user)
    notifications = UserNotifications.objects.filter(user = request.user)
    if request.method == 'POST':
        name = request.POST.get('name','')
        if user.first_name != name:
            notifications = UserNotifications(
                user = request.user,
                method = NotificationsMethod.Name
            )
            notifications.save()
        surname = request.POST.get('surname','')
        if user.last_name != surname:
            notifications = UserNotifications(
                user = request.user,
                method = NotificationsMethod.Surname
            )
            notifications.save()
        address = request.POST.get('address','')
        if userProfil.user_address != address:
            notifications = UserNotifications(
                user = request.user,
                method = NotificationsMethod.Address
            )
            notifications.save()
        email = request.POST.get('email','')
        if user.email != email:
            notifications = UserNotifications(
                user = request.user,
                method = NotificationsMethod.Email
            )
            notifications.save()
        phone = request.POST.get('phone','')
        if userProfil.phone != phone:
            notifications = UserNotifications(
                user = request.user,
                method = NotificationsMethod.Phone
            )
            notifications.save()
        
        user.first_name = name
        user.last_name = surname
        user.email = email
        user.save()
        userProfil.user_address = address
        userProfil.phone = phone
        userProfil.save()
        
    return redirect('my-profil')

@login_required(login_url='account:login')
def my_settings(request):
    order = Order.objects.filter(customers=request.user, status=False)
    order_count = order.count()
    user_order_summary, created = UserOrderSummary.objects.get_or_create(user=request.user)
    user_order_summary.get_orders_by_customer(request.user)
    wishlist = MyWishList.objects.get(user=request.user)
    wish_pro = set(wishlist.products.values_list('id', flat=True))
    wish_count = len(wish_pro)
    if user_order_summary.discounts:
        user_order_summary.get_orders_discount(user_order_summary.discounts)
      
    context={
        'user_order_summary':user_order_summary,
        'order':order,
        'order_count':order_count,
        'wish_pro':wish_pro,
        'wish_count':wish_count,
    }
    return render(request,'settings.html',context)

@login_required(login_url='account:login')
def notifications(request):
    notifications= UserNotifications.objects.filter(user=request.user).order_by('-date')
    order = Order.objects.filter(customers=request.user, status=False)
    order_count = order.count()
    user_order_summary, created = UserOrderSummary.objects.get_or_create(user=request.user)
    user_order_summary.get_orders_by_customer(request.user)
    wishlist = MyWishList.objects.get(user=request.user)
    wish_pro = set(wishlist.products.values_list('id', flat=True))
    wish_count = len(wish_pro)
    if user_order_summary.discounts:
        user_order_summary.get_orders_discount(user_order_summary.discounts)
      
    context={
        'notifications':notifications,
        'user_order_summary':user_order_summary,
        'order':order,
        'order_count':order_count,
        'wish_pro':wish_pro,
        'wish_count':wish_count
    }
    return render(request,'notifications.html',context)

def add_place_order(request):
    notifications = UserNotifications.objects.filter(user=request.user)
    order = Order.objects.filter(customers=request.user)
    place = OrdersPlace.objects.filter(customers=request.user,status=False) 
    user_order_summary, created = UserOrderSummary.objects.get_or_create(user=request.user)
    for ord in order:
        place = OrdersPlace(
            customers = request.user,
            product = ord.product,
            quantity = ord.quantity,
            price = ord.price,
            delivery = ord.delivery,
            discounts = ord.discounts,
            status = False
            
        )
        place.save()
        ord.delete()
    user_order_summary.discount_value = 0
    user_order_summary.discounts = None
    user_order_summary.subtotal = 0
    user_order_summary.total_delivery_cost = 0
    user_order_summary.grand_total = 0 
    user_order_summary.save()
    
    notifications = UserNotifications(
        user = request.user,
        method = NotificationsMethod.OrderPlaced,
    )
    notifications.save()
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



@login_required(login_url='account:login')
def manage_address_view(request):
    address = UserAddress.objects.filter(user=request.user)
    order = Order.objects.filter(customers=request.user, status=False)
    order_count = order.count()
    user_order_summary, created = UserOrderSummary.objects.get_or_create(user=request.user)
    user_order_summary.get_orders_by_customer(request.user)
    wishlist = MyWishList.objects.get(user=request.user)
    wish_pro = set(wishlist.products.values_list('id', flat=True))
    wish_count = len(wish_pro)
    if user_order_summary.discounts:
        user_order_summary.get_orders_discount(user_order_summary.discounts)
      
    context={
        'user_order_summary':user_order_summary,
        'order':order,
        'order_count':order_count,
        'wish_pro':wish_pro,
        'wish_count':wish_count,
        'address':address,
    }
    return render(request,'manage_address.html',context)

@login_required(login_url='account:login')
def saved_cards_view(request):
    
    payments = Payments.objects.filter(user=request.user)
    order = Order.objects.filter(customers=request.user, status=False)
    order_count = order.count()
    user_order_summary, created = UserOrderSummary.objects.get_or_create(user=request.user)
    user_order_summary.get_orders_by_customer(request.user)
    wishlist = MyWishList.objects.get(user=request.user)
    wish_pro = set(wishlist.products.values_list('id', flat=True))
    wish_count = len(wish_pro)
    if user_order_summary.discounts:
        user_order_summary.get_orders_discount(user_order_summary.discounts)
      
    context={
        'user_order_summary':user_order_summary,
        'order':order,
        'order_count':order_count,
        'wish_pro':wish_pro,
        'wish_count':wish_count,
        'payments':payments,
    }
    
    return render(request,'saved_cards.html',context)



