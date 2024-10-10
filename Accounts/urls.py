from django.urls import path
from Accounts.views import *

urlpatterns = [
    path('login/',login_page,name="LoginPage"),
    path('register/',register_page,name="Registration"),
    path('activate/<email_token>/',activate_email,name="Activate_email"),
    path('add-to-cart/<uid>/', add_to_cart , name="add_to_cart" ),
]