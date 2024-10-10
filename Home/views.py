from django.shortcuts import render
from Product.models import Product

# Create your views here.
def home(request):
    
    context = {'products' : Product.objects.all()}
    return render(request , 'Home/index.html', context)