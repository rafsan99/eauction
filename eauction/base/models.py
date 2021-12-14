from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Product(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    photo = models.ImageField(null=True, blank=True, upload_to='images/')
    minimum_bid_price = models.IntegerField()
    auction_end_time = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.name

class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    bidding_price = models.IntegerField(null=True)

    