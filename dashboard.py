import streamlit as st
from core.data_fetcher import fetch_yahoo
from core.indicators import add_indicators
from core.signal_logic import analyze_pair

st.title("📊 Forex Prediction Dashboard")

pairs = ["EURUSD", "GBPUSD", "USDJPY", "USDCHF", "AUDUSD", "USDCAD", "NZDUSD"]

for pair in pairs:
    st.subheader(pair)
    try:
        ticker = f"{pair}=X"
        df = fetch_yahoo(ticker)
        df = add_indicators(df)
        result = analyze_pair(df)
        st.write(result)
    except Exception as e:
        st.error(f"❌ Error fetching or processing data for {pair}: {e}")
