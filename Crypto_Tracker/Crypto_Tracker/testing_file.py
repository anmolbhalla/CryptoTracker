import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Crypto_Tracker.settings")
import django
django.setup()

from Crypto_Tracker.cryptodisplay import models

print('Hello')