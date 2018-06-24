from django.contrib import admin
from django.urls import path, include
from storeapp.views import *


urlpatterns = [
    path('', index, name='index'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
    # path('accounts/logout/', include('storeapp.urls')),
]