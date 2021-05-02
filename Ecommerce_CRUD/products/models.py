from django.db import models
from django import forms
from datetime import datetime
from django.contrib.postgres.fields import ArrayField
# Create your models here.
OFFERS = [('10% OFF WITH CREDIT CARDS','10% OFF WITH CREDIT CARDS'),('RS.100 CASHBACK','RS.100 CASHBACK'),('FREE SHIPPING','FREE SHIPPING'),]
CATEGORY =[('Mobile Phone','MOBILE PHONE'),('Clothing','CLOTHING'),('Laptop','LAPTOP'),('Food','FOOD')]
WARRANTY =[('No Warranty','No Warranty'),('3 Months Warranty','3 Months Warranty'),('6 Months Warranty','6 Months Warranty'),('1 Year Warranty','1 Year Warranty')]

class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    photo = models.ImageField(upload_to='img/',default = '1.png', db_column='Image')
    category = models.CharField(choices=CATEGORY,max_length=100,blank=True)
    manufacturer = models.CharField(max_length=300,blank=True)
    date_manufactured = models.DateField(default=datetime.now)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    availablity = models.BooleanField(default=False)
    warranty = models.CharField(default='No Warrnaty',max_length=50) 
    offers = ArrayField(models.CharField(max_length=200),size = 3)
     
     
    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_edit', kwargs={'pk': self.pk})
