from django.urls import path
from . import views

urlpatterns = [
    path('bitcoin/', views.bitcoin_price, name='bitcoin_price'),
    path('ethereum/', views.ethereum_price, name='ethereum_price')
]