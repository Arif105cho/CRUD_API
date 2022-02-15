from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser,AbstractBaseUser


# Create your models here.


class User(AbstractUser):
    mobile_no = models.CharField(max_length=12)
    address = models.TextField(max_length=300)
    pin_code = models.CharField(max_length=6)
    city = models.CharField(max_length=100)
    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, default=True, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, default=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=350)
    price = models.IntegerField()
    image = models.ImageField(upload_to='shop/images')
    product_desc = models.CharField(max_length=300)
    publish_date = models.DateField()
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class Add_card(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.product)


class DeliveryOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Add_card, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.order)

class Payment(models.Model):
    through=(('1','Card'),('2','UPI'),('3','Online'))
    status=(('1','Success'),('2','pending'),('3','failed'))
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    payment_through= models.CharField(max_length=2, choices=through)
    transection_status= models.CharField(max_length=2, choices=status)
    transection_date=models.DateTimeField()
    def __str__(self):
        return str(self.transection_status)






