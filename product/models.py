from django.db import models
from django.contrib.auth.models import User
class Product(models.Model):
    CATEGORY_CHOICES=[
        ('MTW','MEN\'S Topwear'),
        ('MBW','MEN\'S Bottomwear'),
        ('MFW','MEN\'S Footwear'),
        ('MA','MEN Accessories'),
        ('WTW','WOMEN\'S Topwear'),
        ('WBW','WOMEN\'S Bottomwear'),
        ('WFW','WOMEN\'S Footwear'),
        ('SA','Saree'),
        ('WMA','WOMEN Accessories'),
        ('ST','Stickers'),
        ('CL','Clocks'),
        ('SP','Showpiece'),
        ('KS','Kitchen storage'),
        ('CB','Cookware & Bakeware'),
        ('MAKE','Makeup'),
        ('SC','Skin Care & Bath'),
        ('HA','Haircare'),
        ('FR','Fragrance'),
        ('MOB','Mobile'),
        ('SW','Smart watch'),
        ('SFT','Soft toys'),
        ('DRE','Dresses'),
        ('KF','Footware'),
        ('BC','Baby care'),
        
        
    ]
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=255,null=True)
    price=models.DecimalField(max_digits=10,decimal_places=2,default=0.0)
    size=models.CharField(max_length=10,default='small')
    image=models.ImageField(upload_to='product_images/',default='no image')
    category=models.CharField(max_length=20,choices=CATEGORY_CHOICES,default='null')
    
    class Meta:
        ordering=['category']    


class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,default=1)
    quantity=models.PositiveIntegerField(default=1)
    
    def total_price(self):
        return self.product.price*self.quantity

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,default=1)
    quantity=models.PositiveIntegerField(default=1)
    
    def total_price(self):
        return self.product.price*self.quantity
    def clear_order_data(self):
        self.delete()

class deatail(models.Model):
    name=models.CharField(max_length=100)
    address=models.TextField()
    payment_method=models.CharField(max_length=100)
    contact_number=models.CharField(max_length=10)
    email=models.EmailField()





    
   
        
        
        
        



























