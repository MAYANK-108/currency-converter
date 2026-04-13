import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()
try:
    api_key = st.secrets["EXCHANGE_API_KEY"]
except:
    api_key = os.getenv("EXCHANGE_API_KEY")

st.title("Currency Converter")

currency_dict = {
    "US Dollar (USD)": "USD",
    "Indian Rupee (INR)": "INR",
    "Euro (EUR)": "EUR",
    "British Pound (GBP)": "GBP",
    "Japanese Yen (JPY)": "JPY",
    "Australian Dollar (AUD)": "AUD",
    "Canadian Dollar (CAD)": "CAD",
    "Chinese Yuan (CNY)": "CNY",
    "UAE Dirham (AED)": "AED",
    "Saudi Riyal (SAR)": "SAR",
    "Russian Ruble (RUB)": "RUB",
    "Swiss Franc (CHF)": "CHF",
    "Singapore Dollar (SGD)": "SGD",
    "New Zealand Dollar (NZD)": "NZD",
    "South Korean Won (KRW)": "KRW",
    "Turkish Lira (TRY)": "TRY",
    "Pakistani Rupee (PKR)": "PKR",
    "Bangladeshi Taka (BDT)": "BDT",
    "Sri Lankan Rupee (LKR)": "LKR",
    "Nepalese Rupee (NPR)": "NPR",
    "Thai Baht (THB)": "THB",
    "Indonesian Rupiah (IDR)": "IDR",
    "Malaysian Ringgit (MYR)": "MYR",
    "Philippine Peso (PHP)": "PHP",
    "South African Rand (ZAR)": "ZAR",
    "Brazilian Real (BRL)": "BRL",
    "Mexican Peso (MXN)": "MXN",
    "Egyptian Pound (EGP)": "EGP",
    "Nigerian Naira (NGN)": "NGN",
    "Kenyan Shilling (KES)": "KES"
}
col1,col2,col3 = st.columns(3)
with col1:
    selected_currency_1 = st.selectbox("From:", list(currency_dict.keys()))
    # st.write("You selected:", selected_currency_1)
    first = st.number_input(f"Enter {selected_currency_1}:",min_value=1)

with col2:
    st.image("https://thumbs.dreamstime.com/b/exchange-arrow-transfer-icon-logo-vector-isloated-white-background-exchange-arrow-transfer-icon-logo-vector-isloated-white-136664232.jpg",width = 200)
with col3:
    selected_currency_2 = st.selectbox("To:", list(currency_dict.keys()))
    target = currency_dict[selected_currency_2]
    # st.write("You selected:", selected_currency_2)


if st.button("Convert"):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{currency_dict[selected_currency_1]}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rate = data["conversion_rates"][target]
        converted = rate * first
        st.success(f"{first} {currency_dict[selected_currency_1]} = {converted:.2f} {target}.")
    else:
        st.error("Failed to Fetch Conversion data")

        