from django.db import models
from django.contrib.auth.models import User
from Base.models import BaseClass
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from Base.emails import send_account_activation_email
from Product.models import *
# Create your models here.

class Profile(BaseClass):
    user = models.OneToOneField(User , on_delete=models.CASCADE , related_name="Profile")
    is_email_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100 , null=True , blank=True)
    profile_image = models.ImageField(upload_to="Profile_imgs")
    
    def get_cart_count(self):
        return CartItems.objects.filter(cart__is_paid = False , cart__user = self.user).count
    
    def __str__(self) -> str:
        return self.user.username

class Cart(BaseClass):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='carts')
    is_paid = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.user.username
    
class CartItems(BaseClass):
    cart = models.ForeignKey(Cart , on_delete=models.CASCADE , related_name='cart_items')
    product = models.ForeignKey(Product , on_delete=models.SET_NULL , null=True , blank=True)
    colour_variant = models.ForeignKey(ColourVariant ,on_delete=models.SET_NULL , null=True , blank=True )
    size_variant = models.ForeignKey(SizeVariant ,on_delete=models.SET_NULL , null=True , blank=True )
    
    

@receiver(post_save , sender = User)
def send_email_token(sender , instance , created , **kwargs):
    try:
        if created:
            email_token = str(uuid.uuid4())
            Profile.objects.create(user = instance , email_token = email_token)
            email = instance.email 
            send_account_activation_email(email , email_token)
            
    except Exception as e:
        print(e)
        
