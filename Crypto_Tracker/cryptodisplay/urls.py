from django.urls import path

from . import views

urlpatterns = [
    path('', views.Detail_Display, name='Detail_Display'),
]