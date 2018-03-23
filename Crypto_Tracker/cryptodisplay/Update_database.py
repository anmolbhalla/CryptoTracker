import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Crypto_Tracker.settings")
django.setup()

from cryptodisplay.models import Cryptos

def Update_Database () :

    delete = Cryptos.objects.all().delete()

    with open('/home/aryan/Documents/Github/CryptoTracker/Crawler/crypto_data.txt') as openfileobject:
        count = 1

        for line in openfileobject:
            line_split = line.split('***')

            add = Cryptos(id=count, crypto_logo=line_split[0] , crypto_graph=line_split[1], crypto_number=line_split[2],
                          crypto_name=line_split[3], crypto_price=line_split[4],
                          crypto_change=line_split[5], crypto_market_cap=line_split[6], crypto_supply=line_split[7],
                          crypto_volume=line_split[8])

            add.save()

            count += 1

print('done')
