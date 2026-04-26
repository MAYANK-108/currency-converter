<img width="1170" height="608" alt="Screenshot 2026-04-26 190822" src="https://github.com/user-attachments/assets/9796012c-ce36-49b0-932d-36e3d441c72e" />
# 💱 Currency Converter

A real-time currency converter web app built with **Python** and **Streamlit**, supporting 30+ world currencies.

## 🌐 Live Demo
👉 **[currency-converter-108.streamlit.app](https://currency-converter-108.streamlit.app)**

---

## ✨ Features

- 🔄 Convert between **30+ global currencies**
- ⚡ Real-time exchange rates via **ExchangeRate API**
- 🖥️ Clean 3-column UI — select currency, enter amount, get result instantly
- 🔐 Secure API key handling via `.env` and `st.secrets`

## 🛠️ Tech Stack

- **Python**
- **Streamlit** — for the web UI
- **Requests** — for API calls
- **ExchangeRate API** — for live exchange rates
- **python-dotenv** — for environment variable management

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/MAYANK-108/currency-converter.git
cd currency-converter
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up your API key
Get a free API key from [exchangerate-api.com](https://www.exchangerate-api.com/)

Create a `.env` file in the root directory:
```
EXCHANGE_API_KEY=your_api_key_here
```

### 4. Run the app
```bash
streamlit run App.py
```

---

## 🌍 Supported Currencies

USD, INR, EUR, GBP, JPY, AUD, CAD, CNY, AED, SAR, RUB, CHF, SGD, NZD, KRW, TRY, PKR, BDT, LKR, NPR, THB, IDR, MYR, PHP, ZAR, BRL, MXN, EGP, NGN, KES

---

## 📁 Project Structure

```
currency-converter/
│
├── App.py              # Main Streamlit app
├── requirements.txt    # Python dependencies
├── .gitignore          # Git ignored files
└── .devcontainer/      # Dev container config
```

---

## 👨‍💻 Author

**Mayank** — BTech CSE Student  
[GitHub](https://github.com/MAYANK-108)
