from django.contrib import admin
from .models import Category_model, Customer_model, Order_model, Product_model

# Register your models here.
admin.site.register(Category_model)
admin.site.register(Customer_model)
admin.site.register(Product_model)
admin.site.register(Order_model)