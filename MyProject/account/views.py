from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        username= request.POST.get('username')
        password= request.POST.get('password')
        
        user=authenticate(username=username,password=password)
        
        if user is not None:
            login(request,user)
            messages.success(request, f'{request.user.first_name} {request.user.last_name}, you are successfully logged in...',extra_tags='login_success')
            return redirect('home')
        
        else:
            if not User.objects.filter(username=username).exists():
                messages.warning(request,'Your username is wrong',extra_tags='username')
                context = {'username':username,'password':password}
                return render(request,'login.html',context)
            else:
                messages.warning(request,'Your password is wrong',extra_tags='password')
            
            context = {'username':username,'password':password}
            return render(request,'login.html',context)
        
    return render(request,'login.html')

def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')
        context = {'name':name,'surname':surname,'email':email,"confirm":confirm,'username':username,'password':password}
        if password != confirm:
            messages.warning(request,'Password and Confirm are not the same.',extra_tags='password')

            return render(request,'signup.html',context)
        
        if User.objects.filter(username=username).exists():
            messages.warning(request,'This username is already in use.',extra_tags='username')
            return render(request, 'signup.html',context)
        
        if User.objects.filter(email=email).exists():
            messages.warning(request,'This email is already in use.',extra_tags='email')
            return render(request, 'signup.html',context)
        
        user = User.objects.create_user(username=username,first_name=name,last_name=surname,email=email, password=password)
        user.save()
        login(request,user)
        messages.success(request,'You have registered successfully.')
        return redirect('home')
    
    return render(request,'signup.html')

def forget_view(request):
    return render(request,'Forget.html')

def logout_view(request):
    logout(request)
    return redirect('account:login')