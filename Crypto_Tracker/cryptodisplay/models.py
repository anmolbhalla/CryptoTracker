from django.db import models


class Cryptos(models.Model):
    crypto_number = models.CharField(max_length=10, null=True)
    crypto_logo = models.CharField(max_length=1000)
    crypto_name = models.CharField(max_length=500)
    crypto_market_cap = models.CharField(max_length=500)
    crypto_price = models.CharField(max_length=500)
    crypto_volume = models.CharField(max_length=500)
    crypto_supply = models.CharField(max_length=500)
    crypto_change = models.CharField(max_length=500)
    crypto_graph = models.CharField(max_length=1000)





# Create your models here.
