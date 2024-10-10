from django.contrib import admin
from Product.models import *
# Register your models here.

admin.site.register(Category)

class ProductImageAdmin(admin.StackedInline):
    model = ProductImage
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name' , 'price' , 'category']
    inlines = [ProductImageAdmin]

@admin.register(ColourVariant)
class ColourVariantAdmin(admin.ModelAdmin):
    list_display = ['colour' , 'price']
    model = ColourVariant

@admin.register(SizeVariant)
class SizeVariantAdmin(admin.ModelAdmin):
    list_display = ['size' , 'price']
    model = SizeVariant
    
admin.site.register(Product , ProductAdmin)
    
admin.site.register(ProductImage)