from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect , HttpResponse
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from .models import *
from Product.models import *

# Create your views here.
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user_obj = User.objects.filter(username = username)
        if not user_obj.exists():
            messages.warning(request, 'Username is not Valid')
            return HttpResponseRedirect(request.path_info)
        
        if not user_obj[0].Profile.is_email_verified:
            messages.warning(request, 'Your Account is not Verified')
            return HttpResponseRedirect(request.path_info)
        
        user_obj = authenticate(username = username , password = password)
        if user_obj:
            login(request , user_obj)
            return redirect('/')
            
        messages.warning(request, 'Invalid Credentials!!!')
    return render(request, 'Account/login.html')

# -------------------------------------------------------------------------------------------------------------

def register_page(request):
    
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user_obj = User.objects.filter(username = username)
        email_obj = User.objects.filter(email = email)
        
        if user_obj.exists():
            messages.warning(request, 'Username already exists please try other Username')
            return HttpResponseRedirect(request.path_info)
        
        if email_obj.exists():
            messages.warning(request, 'Entered Email is already Registered')
            return HttpResponseRedirect(request.path_info)
        
        user_obj = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
            email = email,
        )
        user_obj.set_password(password)
        user_obj.save()
        messages.warning(request, 'A mail has been sent to your email for Verification.')
        return HttpResponseRedirect(request.path_info)
    
    return render(request, 'Account/register.html')

def activate_email(request , email_token):
    try:
        user = Profile.objects.get(email_token = email_token)
        user.is_email_verified = True
        user.save()
        return redirect('/')
    except Exception as e:
        return HttpResponse('This is an Invalid Email Token')
    
@login_required  
def add_to_cart(request , uid):
    variant = request.GET.get('variant')
    
    product = Product.objects.get(uid = uid)
    user = request.user
    cart , _ = Cart.objects.get_or_create(user = user , is_paid = False)

    cart_item = CartItems.objects.create(cart = cart , product = product ,)
    
    if variant:
        variant = request.GET.get('variant')
        size_variant = SizeVariant.objects.get(size = variant)
        cart_item.size_variant = size_variant
        cart_item.save()
        
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
