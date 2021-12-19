from django.forms import ModelForm
from .models import Product, Bid

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'photo', 'minimum_bid_price', 'auction_end_time']

class BidForm(ModelForm):
    class Meta:
        model = Bid
        fields = ['bidding_price']