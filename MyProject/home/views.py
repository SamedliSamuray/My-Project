from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect , get_object_or_404
from .models import *
from django.db.models import Q , Avg , Count
from .forms import *
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
# Create your views here.

def home_view(request):
    order = Order.objects.filter(customers=request.user, status=False)
    return render(request,'base.html',{'order':order})

def products_view(request):
    order = Order.objects.filter(customers=request.user, status=False)
    products_category = Products_Categories.objects.annotate( items_count = Count('products') )
    brands = Brand.objects.annotate( items_count = Count('products') )
    colors = Color.objects.annotate( items_count = Count('products') )
    products = Products.objects.all().annotate(average_rating=Avg('comments__rating'))
    
    # filter_category = request.GET.getlist('category')
    # filter_brand = request.GET.getlist('brand')
    # filter_color = request.GET.getlist('color')
    # filter_price_min = request.GET.get('range-min')
    # filter_price_max = request.GET.get('range-max')

    # django products filters
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
    
    context={'order':order,'products_category':products_category,'brands':brands,"colors":colors,'products':products}
    return render(request,'products.html',context)

def product_details(request, id):
    product = get_object_or_404(Products, id=id)
    products = Products.objects.filter(name=product.name, brand=product.brand).exclude(color=product.color)
    related = Products.objects.filter(Q(brand=product.brand) | Q(materials=product.materials) | Q(category=product.category)).exclude(id=id)
    colors = Color.objects.all()
    orders = Order.objects.filter(customers=request.user, status=False)
    comments = product.comments.all()
    average_rating = comments.aggregate(Avg('rating'))['rating__avg'] or 0
    
    
    if request.method == 'POST':
       if 'comment_name' in request.POST:
            comment_content = request.POST.get('comment_content')
            rating = int(request.POST.get('rating'))
            
            comment_name = request.POST.get('comment_name')

            new_comment = Comment(
            comment_name=comment_name,
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
        'order':orders,
        'product': product,
        'colors': colors,
        'products': products,
        'related': related,
        'comments': comments,
        'average_rating': average_rating,
    }
    return render(request, 'product_details.html', context)

@login_required
def delete_order(request,id):
    order = get_object_or_404(Order,id=id)
    order.delete()
    user_order_summary = UserOrderSummary.objects.get(user=request.user)
    user_order_summary.get_orders_by_customer(request.user)
    if user_order_summary.subtotal==0:
        user_order_summary.discount_value=0
    user_order_summary.grand_total = user_order_summary.grand_total-user_order_summary.discount_value
    user_order_summary.save()
    
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
        user_order_summary = UserOrderSummary.objects.get(user=request.user)
        user_order_summary.get_orders_by_customer(request.user)
        user_order_summary.grand_total = user_order_summary.grand_total-user_order_summary.discount_value
        user_order_summary.save()
        
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))    



def checkout_view(request):
   
    order = Order.objects.filter(customers=request.user, status=False)
    user_order_summary = UserOrderSummary.objects.get(user=request.user)
    user_order_summary.get_orders_by_customer(request.user)
            
    context={
        'user_order_summary':user_order_summary,
        'order':order,
    }
    return render(request,'checkout.html',context)

def shipping_view(request):
    order = Order.objects.filter(customers=request.user, status=False)
    user_order_summary = UserOrderSummary.objects.get(user=request.user)
    address = UserAddress.objects.filter(user=request.user)
    if request.method == 'POST':
        id=request.POST.get('default_adress')
        default_address = UserAddress.objects.get(id=id)
        user_order_summary.address = default_address
        user_order_summary.save()
        return redirect('payments')
    context={'address':address,'user_order_summary':user_order_summary,'order':order}
    return render(request,'shipping.html',context)
def apply_discount(request):
    order = Order.objects.filter(customers=request.user, status=False)
    user_order_summary = UserOrderSummary.objects.get(user=request.user)
    discount_code = request.POST.get('discount_code')
    messages
    user_order_summary.discount_value=0.00
    user_order_summary.get_orders_by_customer(customers=request.user)
    discount_value = 0
    discount=discount_code
    if discount_code and user_order_summary.subtotal>0: 
        try:
            discount= Discounts.objects.get(code=discount_code,is_active=True)
            if discount.discount_type == "percentage":
               discount_value= min((user_order_summary.grand_total*discount.discount_amount)/100,discount.max_discount_amount)
               
            
            elif discount.discount_type == 'fixed':
               discount_value= discount.discount_amount
            user_order_summary.grand_total=user_order_summary.grand_total-discount_value
            user_order_summary.discount_value=discount_value
            user_order_summary.discounts=discount
            user_order_summary.save()
            for ord in order:
                ord.discounts=discount
                ord.save()
            
            messages.success(request, f'{discount_code} code successfully redeemed, discount ${discount_value}.')
        except Discounts.DoesNotExist:
            messages.warning(request,f'"{discount_code}" code is invalid')
    elif not discount_code and user_order_summary.subtotal>0:
        
        messages.warning(request, 'You have not entered a discount code.')
    else:
        messages.warning(request, 'There are currently no items in your cart..')
        
    # context = {
    #     'discount':discount,
    #     "user_order_summary":user_order_summary,
    #     'order':order,
    #     'discount_value':discount_value,
    # }
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    # return render(request, 'checkout.html', context)
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
    user_order_summary = UserOrderSummary.objects.get(user=request.user)
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
    context={'address':address,'user_order_summary':user_order_summary,'update_address': update_address,'order':order}
    return render(request, 'shipping.html',context)
    
def payments_view(request):
    order = Order.objects.filter(customers=request.user, status=False)
    user_order_summary = UserOrderSummary.objects.get(user=request.user)
    address = UserAddress.objects.filter(user=request.user)
    context={'address':address,'user_order_summary':user_order_summary,'update_address': update_address,'order':order}
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
            
        else:
            paymants_card = Payments.objects.create(user=request.user,name=name,payment_method=payment_method,amount=amount)
        paymants_card.save()
        user_order_summary.payments = paymants_card
        user_order_summary.save()
    return render(request,'payment.html')