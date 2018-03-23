from django.shortcuts import render
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

def index (request):
    return HttpResponse("Welcome to crypto display")
# Create your views here.
