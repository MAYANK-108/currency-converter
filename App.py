import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key= os.getenv("EXCHANGE_API_KEY")

st.title("Currency Converter")
usd = st.number_input("Enter(in USD):",min_value=1)
target = st.selectbox("Convert to",["INR","EUR","GBP","JPY","CAD"])

if st.button("Convert"):
    url = "https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rate = data["conversion_rates"][target]
        converted = rate * usd
        st.success(f"{usd} USD = {converted:.2f} {target}.")
    else:
        st.error("Failed to Fetch Conversion data")

        