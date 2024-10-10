from django.contrib import admin
from Accounts.models import Profile , Cart , CartItems
# Register your models here.

admin.site.register(Profile)

admin.site.register(Cart)

class CartItemsAdmin(admin.ModelAdmin):
    list_display = ('product', 'colour_variant', 'size_variant')
admin.site.register(CartItems , CartItemsAdmin)
