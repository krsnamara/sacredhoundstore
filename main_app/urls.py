from django.urls import path
from . import views

# app_name = 'sacred_hound_store'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('shop/', views.shop, name='shop'),
    path('contact/', views.contact, name='contact'),
    path('shop/<int:items_id>/', views.item_detail, name='detail'),
    # path('shop/create/', views.Items.as_view(), name='items_create'),
    # path('shop/<int:pk>/update/', views.ItemsUpdate.as_view(), name='items_update'),
    # path('shop/<int:pk>/delete/', voews.ItemsDelete.as_view(), name='items_delete'),
]