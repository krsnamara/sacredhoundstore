from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Items
from django.http import HttpResponse

# TODO adding the ability to have seller update and upload pictures of product
# import boto3
# import uuid 

# S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
# BUCKET = 'catcollector-stardust-0217-bucket'

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def shop(request):
    items = Items.objects.filter(user=request.user)
    return render(request, 'items/shop.html', { 'items': items})

def contact(request):
    return render((request), 'contact.html')

def item_detail(request, items_id):
    item = Items.objects.get(id=items_id)
    return render(request, 'items/detail.html', {
        'items': items,
    })
