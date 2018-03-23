from django.shortcuts import render
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Cryptos

def index (request):

    cryptos_detail = Cryptos.objects.order_by('id')
    template = loader.get_template('cryptodisplay/home.html')
    context = {
        'cryptos_detail': cryptos_detail,
    }
    with open('/home/anmol/Documents/Github/CryptoTracker/Crawler/crypto_data.txt') as openfileobject:
        for line in openfileobject:
            line_split = line.split('***')
            add=Cryptos(crypto_logo = line_split[0], crypto_graph = line_split[1], crypto_number = line_split[2], crypto_name = line_split[3], crypto_price = line_split[4],
                        crypto_change = line_split[5], crypto_market_cap = line_split[6], crypto_supply = line_split[7], crypto_volume = line_split[8]

                        )
            add.save()

    return HttpResponse(template.render(context, request))


# Create your views here.
