from storeapp.models import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html')

def login_user(request):
    if request.method == 'POST':
        username, password = request.POST.get('username'), request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')

def logout_user(request):
    logout(request)
    redirect('index')

def register_user(request):
    if request.method == 'POST':
        details = request.POST
        import ipdb
        ipdb.set_trace()
        user = User.objects.create_user(
            username=details['username'],
            password=details['password'],
            email=details['email'],
        )
        user.save()
        user = authenticate(
            request,
            username=details['username'],
            password=details['password']
        )
        if user:
            login(request, user)
            return redirect('index')
    else:
        return render(request, 'register.html')

def contact(request):
    return render(request, 'contact.html')

def basket(request):
    return render(request, 'basket.html')

def category(request):
    return render(request, 'category.html')

def detail(request):
    return render(request, 'detail.html')

def blog(request):
    return render(request, 'blog.html')

def post(request):
    return render(request, 'post.html')

def text(request):
    return render(request, 'text.html')

def text_right(request):
    return render(request, 'text-right.html')

def faq(request):
    return render(request, 'faq.html')

def men(request):
    return render(request, 'men.html')

def women(request):
    return render(request, 'women.html')

def not_found_404(request):
    return render(request, '404.html')

def category_right(request):
    return render(request, 'category-right.html')

def category_full(request):
    return render(request, 'category-full.html')

def customer_order(request):
    return render(request, 'customer-order.html')

def customer_orders(request):
    return render(request, 'customer-orders.html')

def customer_wishlist(request):
    return render(request, 'customer-wishlist.html')

def customer_account(request):
    return render(request, 'customer-account.html')

def checkout(request, no):
    return render(request, 'checkout{0}.html'.format(no))