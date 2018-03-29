from django.shortcuts import render
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Cryptos
from .models import Cryptos_details

def Detail_Display (request):

    cryptos_detail = Cryptos.objects.order_by('id')
    template = loader.get_template('cryptodisplay/index.html')
    context = {
        'cryptos_detail': cryptos_detail,
    }


    return HttpResponse(template.render(context, request))

def get_log(request):
    cryptos_detail = Cryptos.objects.order_by('id')
    template = loader.get_template('cryptodisplay/table.html')
    context = {
        'cryptos_detail': cryptos_detail,
    }

    return HttpResponse(template.render(context, request))

def details(request,crypto_name):
    details_crypto=Cryptos_details.objects.filter(details_crypto_name=crypto_name)
    template=loader.get_template('cryptodisplay/details.html')
    context={
        'details_crypto':details_crypto,
    }
    return HttpResponse(template.render(context,request))