from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Product, Bid
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import ProductForm, BidForm
from datetime import datetime
import time
# Create your views here.

def loginPage(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
         
        except:
             messages.error(request, 'user does not exist')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
            messages.error(request, 'Username or Password does not match')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    
    form = UserCreationForm()
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred')
    return render(request, 'base/login_register.html', {'form': form})

@login_required(login_url='login')
def home(request):
    data = Product.objects.all()
    pro = {
        "products" : data
    }
    return render(request, 'base/home.html', pro)

def createProduct(request):
    form = ProductForm()
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form' : form}
    return render(request, 'base/product_form.html', context)

def product(request, pk):
    current_time=datetime.now()
    current_time = current_time.strftime('%Y-%m-%d')
    
    product = Product.objects.get(id=pk)
    bid_prices = product.bid_set.all()
    end_time = product.auction_end_time
    end_time = end_time.strftime('%Y-%m-%d')
    
    data = request.POST.get('body')
    price = product.minimum_bid_price

    if request.method == "POST": 
        if int(data) >= price:
            bid = Bid.objects.create(
                user = request.user,
                product = product,
                bidding_price = request.POST.get('body')
            )
            return redirect('product',pk=product.id)
        else:
            messages.error(request, 'Please enter valid bid price')
    
    
    #winner = max(bid_prices.bidding_price)
    maxbid = 0
    maxbidder = "Nobody"
    for bid_price in bid_prices:
        if bid_price.bidding_price > maxbid :
            maxbid = bid_price.bidding_price
            maxbidder = bid_price.user
    
    winner = maxbidder

    bidding_number = 0
    for bid_price in bid_prices:
        if bid_price.user == request.user :
            bidding_number = 1


    context = {'product': product , 'bid_prices' : bid_prices, 'winner' : winner, 'maxbid' : maxbid, 'current_time' : current_time, 'end_time' : end_time, 'bidding_number' : bidding_number }
    return render(request, 'base/product.html', context)


@login_required(login_url='login')
def editBid(request, pk):
    bid = Bid.objects.get(id=pk)
    form = BidForm(instance=bid)

    if request.user != bid.user:
        return HttpResponse('You are not allowed here!!')

    if request.method == "POST":
        form = BidForm(request.POST, instance=bid)
        if form.is_valid():
            if bid.product.minimum_bid_price <= form.cleaned_data.get("bidding_price"):
                form.save()
                return redirect('home')
            else:
                messages.error(request, 'Please enter valid bid price')
    context = {'form':form}
    return render(request, 'base/bid_form.html', context)