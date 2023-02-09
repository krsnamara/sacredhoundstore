from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Item, CartItem, Cart
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
def carts(request):
    carts = Cart.objects.filter(user=request.user)
    return render(request, 'cart/cart.html', {'carts': carts})

@login_required
def carts_detail(request, cart_id):
  cart = Cart.objects.get(id=cart_id)
  #instantiant the feeding form
  item_cart_doesnt_have = item.objects.exclude(id__in=cart.items.all().values_list('id'))
  return render(request, 'carts/detail.html', {
    'cart': cart,
    'items': items_cart_doesnt_have
  })

def item_detail(request, item_id):
    item = Item.objects.get(id=item_id)
    # cartitem_form = CartItemForm()
    return render(request, 'items/detail.html', {
        'item': item,
        # 'cartitem_form': cartitem_form,
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

@login_required
def assoc_item(request, cart_id, item_id):
    Cart.objects.get(id=cart_id).items.add(item_id)
    return redirect('detail', cart_id=cart_id)

class ItemCreate(LoginRequiredMixin, CreateView):
    model = Item
    fields = ('__all__')
    success_url = '/shop/'

    def form_valid(self, form):
        form.instance.user =self.request.user
        return super().form_valid(form)

class ItemUpdate(LoginRequiredMixin, UpdateView):
    model = Item
    fields = '__all__'

class ItemDelete(LoginRequiredMixin, DeleteView):
    model = Item
    success_url = '/shop/'

class CartCreate(LoginRequiredMixin, CreateView):
    model = Cart
    fields = ('name')
    success_url = '/shop/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)    

class CartUpdate(LoginRequiredMixin, UpdateView):
  model = Cart
  fields = ('name')

class CartDelete(LoginRequiredMixin, DeleteView):
  model = Cart
  success_url = '/carts/'

#  THE GRAVEYARD 

# @login_required
# def cart(request, cart_id):
#     cart = Cart.objects.get(id=cart_id)
#     items_cart_has = Item.objects.include(id__in=cart.items.all().values_list('id'))
#     return render(request, 'cart/cart.html', {'carts': carts, 'items': items_cart_has})

# @login_required
# def add_to_cart(request, item_id):
#     Cart.objects.get(id=cart_id).items.add(item_id)
#     return redirect('shop')

# @login_required
# def add_to_cart(request, item_id):
#     item = get_object_or_404(Item, pk=item_id)

#     cart, created = Cart.objects.get_or_create(user=request.user)
#     cart_item, created = CartItem.objects.get_or_create(cart=cart, item=item)
#     if not created:
#         cart_item.quantity += 1
#         cart_item.save()
#     return redirect('cart')



# class CartUpdate(LoginRequiredMixin, UpdateView):
#     model = Cart
#     fields = ('__all__')

# class CartDelete(LoginRequiredMixin, DeleteView):
#     model = Cart
#     success_url = '/cart/'