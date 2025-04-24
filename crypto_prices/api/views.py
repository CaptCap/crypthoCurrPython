import requests
from django.shortcuts import render
def get_cryptocurrency_data(coin_id):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data[coin_id]['usd'] 

def bitcoin_price(request):
    price = get_cryptocurrency_data('bitcoin')
    context = {'price': price}
    return render(request, 'bitcoin_price.html', context)
def ethereum_price(request):
    price = get_cryptocurrency_data('ethereum')
    return render(request, 'ethereum_price.html', {'price': price})