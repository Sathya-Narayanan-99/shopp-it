from django.contrib import admin
from .models import *

# Register your models here.
admin.site.admin.site.register(Customer)
admin.site.admin.site.register(Product)
admin.site.admin.site.register(Cart)
admin.site.admin.site.register(CartItems)
admin.site.admin.site.register(ShippingAddress)