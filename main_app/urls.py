from django.urls import path
from . import views

# app_name = 'sacred_hound_store'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('shop/', views.shop, name='shop'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.cart, name='cart'),
    path('shop/<int:item_id>/', views.item_detail, name='detail'),
    path('shop/create/', views.ItemCreate.as_view(), name='item_create'),
    path('shop/<int:pk>/update/', views.ItemUpdate.as_view(), name='item_update'),
    path('shop/<int:pk>/delete/', views.ItemDelete.as_view(), name='item_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]