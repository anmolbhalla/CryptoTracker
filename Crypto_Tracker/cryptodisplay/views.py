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
<<<<<<< HEAD
=======
    with open('/home/aryan/Documents/Github/CryptoTracker/Crawler/crypto_data.txt') as openfileobject:
        for line in openfileobject:
            line_split = line.split('-')
           # print(line_split)
            add=Cryptos(crypto_logo=line_split[0],crypto_graph=line_split[1],crypto_name=line_split[3],crypto_market_cap=line_split[3],
                        crypto_price=line_split[4],crypto_volume=line_split[5],crypto_supply=line_split[6]

                        )
            add.save()
>>>>>>> 7942dfa41a7710233ae271c998eebc6cb159a27e

    return HttpResponse(template.render(context, request))


# Create your views here.
