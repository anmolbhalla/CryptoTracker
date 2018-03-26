import django
import os
import time
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Crypto_Tracker.settings")
django.setup()

from cryptodisplay.models import Cryptos

def Update_Database () :

    #delete = Cryptos.objects.all().delete()

    with open('/home/aryan/Documents/Github/CryptoTracker/Crawler/crypto_data.txt') as openfileobject:
        #count = 1

        for line in openfileobject:
            line_split = line.split('***')
            #print(line_split[2])




Update_Database()