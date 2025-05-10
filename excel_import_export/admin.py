from django.contrib import admin 
from django.db import models
from . import models as app_models


# Register your models here.


# @admin.register(app_models.ProductItem)
# class  ProductItemAdmin(admin.ModelAdmin): 
#     list_displa =["title","get_image_link","description","price","sale_price","shipping_cost","link"]
#         
#    


for model in app_models.__dict__.values():
    if isinstance(model, type) and issubclass(model, models.Model):
        if isinstance(model,app_models.ProductItem):
            continue 
        admin.site.register(model) 



