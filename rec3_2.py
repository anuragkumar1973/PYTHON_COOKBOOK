# streamlit_app.py
import streamlit as st
import requests

API_URL = "https://api.exchangerate-api.com/v4/latest/{}"

@st.cache_data(show_spinner=False)
def fetch_rates(base: str):
    resp = requests.get(API_URL.format(base), timeout=10)
    resp.raise_for_status()
    return resp.json()

# get currency list once (use USD as a safe default)
try:
    base_data = fetch_rates("USD")
    currencies = sorted(base_data["rates"].keys())
except Exception as e:
    st.title("Currency Converter")
    st.error(f"Could not load currency list: {e}")
    st.stop()

st.title("Currency Converter")

col1, col2 = st.columns(2)
with col1:
    source = st.selectbox("Source currency", currencies, index=currencies.index("USD") if "USD" in currencies else 0)
with col2:
    target = st.selectbox("Target currency", currencies, index=currencies.index("EUR") if "EUR" in currencies else 0)

# fetch rates for selected source and display conversion rate
try:
    with st.spinner("Fetching latest rates..."):
        data = fetch_rates(source)
    rate = data["rates"].get(target)
    if rate is None:
        st.error(f"No rate available for {target}")
    else:
        st.subheader(f"1 {source} = {rate:.6f} {target}")
        # optional: show inverse
        inv = 1 / rate if rate != 0 else None
        if inv:
            st.write(f"1 {target} = {inv:.6f} {source}")
        if "time_last_updated" in data:
            import datetime
            ts = datetime.datetime.fromtimestamp(data["time_last_updated"])
            st.caption(f"Rates last updated: {ts}")
except requests.RequestException as e:
    st.error(f"Network error while fetching rates: {e}")
except Exception as e:
    st.error(f"Unexpected error: {e}")