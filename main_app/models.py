from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    materials = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    price = models.IntegerField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('detail', kwargs={'item_id': self.id})