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
    value_change=models.CharField(max_length=100)





# Create your models here.

# name_crypto_id = Cryptos.objects.get(crypto_number=line_split[2])
#
# if (name_crypto_id.crypto_name != line_split[3] or name_crypto_id.crypto_price != line_split[
#     4] or name_crypto_id.crypto_change != line_split[5] or name_crypto_id.crypto_market_cap != line_split[
#     6] or name_crypto_id.crypto_supply != line_split[7])
