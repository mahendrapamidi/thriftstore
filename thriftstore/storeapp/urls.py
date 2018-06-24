from django.contrib import admin
from django.urls import path, include
from storeapp.views import *


urlpatterns = [
    path('accounts/login/', ),
    path('accounts/logout/', include('storeapp.urls')),
]