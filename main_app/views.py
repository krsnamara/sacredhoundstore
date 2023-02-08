from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Item
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
    items = Item.objects.all()
    return render(request, 'items/shop.html', { 'items': items})

def contact(request):
    return render((request), 'contact.html')

@login_required
def cart(request):
    return render((request), 'cart/cart.html')

def item_detail(request, item_id):
    item = Item.objects.get(id=item_id)
    return render(request, 'items/detail.html', {
        'item': item,
    })

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('shop')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


class ItemCreate(CreateView):
    model : Item
    fields = ('__all__')
    success_url = '/shop/'

    def form_valid(self, form):
        form.instance.user =self.request.user
        return super().form_valid(form)

