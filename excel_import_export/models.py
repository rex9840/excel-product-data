from django.db import models

# Create your models here.



class ItemAvailablity(models.TextChoices):
    IN_STOCK = ("IN_S" ,"in_stock")
    OUT_OF_STOCK = ("OUT_S","out_of_stock")
    



class ItemGroup(models.Model): 
    name = models.CharField(null=False,blank=False,unique=True)
    remarks = models.CharField(null=True,blank=True)
    
    def __str__(self):
        return str(self.name)
    

class ProductItems(models.Model): 
    product_id = models.CharField(null=False,blank=False,unique=True)
    title = models.CharField(max_length=250,null=False,blank=False)
    image_link = models.CharField(max_length=250,null=False,blank=False)
    description = models.TextField(null=True,Blank=True)
    link = models.CharField(max_length=250,null=False,blank=False)
    price = models.CharField(null=False,blank=False)
    sale_price =  models.CharField(null=False,blank=False) 
    shipping_cost =  models.CharField(null=False,blank=False) 
    item_group = models.ForeignKey("ItemGroup",on_delete=models.SET_NULL,related_name="item_group",)
    availability = models.CharField(choices=ItemAvailablity.choices,default=ItemAvailablity.OUT_OF_STOCK)
    
    
    
    
    
    
    
    
    
    


class Logs(models.Model):
    pass 
 


 
