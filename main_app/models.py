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
    quantity = models.IntegerField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'cartItem_id': self.id})     

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_item = models.ForeignKey(CartItem, on_delete=models.CASCADE)