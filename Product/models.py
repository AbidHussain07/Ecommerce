from django.db import models
from Base.models import *
from django.utils.text import slugify

# Create your models here.
class Category(BaseClass):
    category_name = models.CharField(max_length=25)
    slug = models.SlugField(unique=True , null=True , blank=True)
    category_image = models.ImageField(upload_to="Categories")

    def save(self , *args , **kwargs):
        self.slug = slugify(self.category_name)
        super(Category,self).save(*args , **kwargs)
        
    def __str__(self) -> str:
        return self.category_name
        
class ColourVariant(BaseClass):
    colour = models.CharField(max_length=20 , null=True , blank=True)
    price = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.colour
    
class SizeVariant(BaseClass):
    size = models.CharField(max_length=20 , null=True , blank=True)
    price = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.size

class Product(BaseClass):
    product_name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True , null=True , blank=True)
    category = models.ForeignKey(Category, related_name = "Product", on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.TextField()
    colour_variant = models.ManyToManyField(ColourVariant)
    size_variant = models.ManyToManyField(SizeVariant)
    
    def save(self , *args , **kwargs):
        self.slug = slugify(self.product_name)
        super(Product,self).save(*args , **kwargs)
        
    def get_product_price_by_size(self , size):
        return self.price + SizeVariant.objects.get(size = size).price
        
    def __str__(self) -> str:
        return self.product_name
    
    
class ProductImage(BaseClass):
    product = models.ForeignKey(Product, related_name = "Product_Images", on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to="Product")