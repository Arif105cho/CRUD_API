from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(User)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(Add_card)
admin.site.register(DeliveryOrder)
admin.site.register(Payment)


