import streamlit as st
import requests

def get_crypto_price(crypto):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=USD"
    response = requests.get(url)
    data = response.json()
    price = data[crypto]['usd']
    return price

st.title("Crypto Price Checker")

crypto_symbol = st.text_input("Enter cryptocurrency symbol (e.g., btc, eth, etc.):")
if crypto_symbol:
    price = get_crypto_price(crypto_symbol)
    st.write(f"The current price of {crypto_symbol.upper()} is ${price}")
