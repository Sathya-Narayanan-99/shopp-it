from django.contrib import admin
from .models import *

#sathya
#TestPass123

# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItems)
admin.site.register(ShippingAddress)