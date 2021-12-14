from django.forms import ModelForm
from .models import Product, Bid

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class BidForm(ModelForm):
    class Meta:
        model = Bid
        fields = ['bidding_price']