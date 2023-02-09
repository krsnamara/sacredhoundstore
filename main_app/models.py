from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

# Order = models.ForeignKey('Order', on_delete=models.CASCADE)

class Item(models.Model):
    name = models.CharField(max_length=100)
    materials = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    price = models.IntegerField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class CartItem(models.Model):
    item = models.OneToOneField(Profile, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(null=True)

    def __str__(self):
        return self.item.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_item = models.ForeignKey(CartItem, on_delete=models.CASCADE)