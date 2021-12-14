from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Product, Bid
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import ProductForm, BidForm
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
    product = Product.objects.get(id=pk)
    bid_prices = product.bid_set.all()
    
    if request.method == "POST":
        bid = Bid.objects.create(
            user = request.user,
            product = product,
            bidding_price = request.POST.get('body')
        )
        return redirect('product',pk=product.id)
    
    context = {'product': product , 'bid_prices' : bid_prices}
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
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'base/bid_form.html', context)