import requests

def get_crypto_price(crypto):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=USD"
    response = requests.get(url)
    data = response.json()
    price = data[crypto]['usd']
    return price

