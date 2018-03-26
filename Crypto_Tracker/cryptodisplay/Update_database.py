import django
import os
import time
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Crypto_Tracker.settings")
django.setup()

from cryptodisplay.models import Cryptos

def Update_Database () :

    #delete = Cryptos.objects.all().delete()

    with open('/home/aryan/Documents/Github/CryptoTracker/Crawler/crypto_data.txt') as openfileobject:
<<<<<<< HEAD
        count = 1
=======
        #count = 1

        for line in openfileobject:
            line_split = line.split('***')
            #print(line_split[2])

            name_crypto_id = Cryptos.objects.get(id=line_split[2])
            print(name_crypto_id.id)
            if (name_crypto_id.crypto_name != line_split[3] or name_crypto_id.crypto_price != line_split[
                4] or name_crypto_id.crypto_change != line_split[5] or name_crypto_id.crypto_market_cap != line_split[
                6] or name_crypto_id.crypto_supply != line_split[7]):
                name_crypto_id.id = line_split[2]
                name_crypto_id.save()
                name_crypto_id.crypto_name = line_split[3]
                name_crypto_id.save()
                name_crypto_id.crypto_price = line_split[4]
                name_crypto_id.save()
                name_crypto_id.crypto_change = line_split[5]
                name_crypto_id.save()
                name_crypto_id.crypto_market_cap = line_split[6]
                name_crypto_id.save()
                name_crypto_id.crypto_supply = line_split[7]
                name_crypto_id.save()
                name_crypto_id.value_change = "1"
                name_crypto_id.save()
            else:
                name_crypto_id.value_change = "0"
                name_crypto_id.save()



#while (True) :
Update_Database()
#time.sleep(120)

