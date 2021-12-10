from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='')
    minimum_bid_price = models.CharField(max_length=20)
    auction_end_time = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.name

