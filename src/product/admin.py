from django.contrib import admin
from .models import Product ,ProductImage ,Category,Alternative,Accessories
# Register your models here.
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(Alternative)
admin.site.register(Accessories)
