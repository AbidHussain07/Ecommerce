from django.urls import path
from Product.views import *
urlpatterns = [
    path('<slug>/',get_product,name="GetProduct"),
]