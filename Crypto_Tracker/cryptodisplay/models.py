from django.db import models


class Cryptos(models.Model):
<<<<<<< HEAD
    crypto_id=models.CharField(max_length=200)
    crypto_logo=models.CharField(max_length=1000)
    crypto_name=models.CharField(max_length=500)
    crypto_market_cap=models.CharField(max_length=500)
    crypto_price=models.CharField(max_length=500)
    crypto_volume=models.CharField(max_length=500)
    crypto_supply=models.CharField(max_length=500)
    crypto_change=models.CharField(max_length=500)
    crypto_graph=models.CharField(max_length=1000)
=======

    crypto_number = models.CharField(max_length=10, null=True)
    crypto_logo = models.CharField(max_length=1000)
    crypto_name = models.CharField(max_length=500)
    crypto_market_cap = models.CharField(max_length=500)
    crypto_price = models.CharField(max_length=500)
    crypto_volume = models.CharField(max_length=500)
    crypto_supply = models.CharField(max_length=500)
    crypto_change = models.CharField(max_length=500)
    crypto_graph = models.CharField(max_length=1000)
>>>>>>> 65493e6d9a35b046cf3a2e6c7dc38d512d81676d





# Create your models here.
