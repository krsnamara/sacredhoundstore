from django.shortcuts import render
from .models import Items
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def items_index(request):
    items = Items.objects.all()
    return render(request, 'items/index.html', { 'items': items})
