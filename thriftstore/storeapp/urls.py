from django.contrib import admin
from django.urls import path, include
from storeapp.views import *


urlpatterns = [
    path('', index, name='index'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
    path('contact/', contact, name='contact'),
    path('basket/', basket, name='basket'),
    path('detail/', detail, name='detail'),
    path('category/', category, name='category'),
    path('blog/', blog, name='blog'),
    path('post/', post, name='post'),
    path('text/', text, name='text'),
    path('text-right/', text_right, name='text_right'),
    path('faq/', faq, name='faq'),
    path('men/', men, name='men'),
    path('women/', women, name='women'),
    path('404/', not_found_404, name='404'),
    path('category-right/', category_right, name='category_right'),
    path('category-full/', category_full, name='category_full'),
    path('customer-orders/', customer_orders, name='customer_orders'),
    path('customer-wishlist/', customer_wishlist, name='customer_wishlist'),
    path('customer-order/', customer_order, name='customer_order'), 
    path('customer-account/', customer_account, name='customer_account'), 
    path('checkout/<int:no>/', checkout, name="checkout")
    # path('accounts/logout/', include('storeapp.urls')),
]