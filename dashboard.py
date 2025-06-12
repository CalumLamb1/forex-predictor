import streamlit as st
import yfinance as yf
from core.indicators import add_indicators
from core.tp_sl import calculate_tp_sl
from core.signal_logic import analyze_pair

st.set_page_config(page_title="Forex Prediction Dashboard", layout="wide")
st.title("📈 Forex Prediction Dashboard")

# Major Forex pairs
pairs = ["EURUSD", "GBPUSD", "USDJPY", "USDCHF", "AUDUSD", "USDCAD", "NZDUSD"]

for pair in pairs:
    st.header(pair)

    try:
        st.write("📊 Fetching data...")
        # Yahoo ticker format (e.g., EURUSD=X)
        ticker = pair + "=X"

        # Download daily and hourly data from Yahoo Finance
        daily_df = yf.download(ticker, period="6mo", interval="1d")
        hourly_df = yf.download(ticker, period="7d", interval="1h")

        if daily_df.empty or hourly_df.empty:
            st.error(f"No data found for {pair}")
            continue

        # Add indicators
        daily_df = add_indicators(daily_df)
        hourly_df = add_indicators(hourly_df)

        # Analyze prediction signal
        signal, confidence = analyze_pair(daily_df, hourly_df)
        tp, sl = calculate_tp_sl(hourly_df)

        # Show results
        st.success(f"Prediction: {signal} | Confidence: {confidence*100:.1f}%")
        st.info(f"Suggested Take Profit: {tp:.5f} | Stop Loss: {sl:.5f}")

        # Optional: show chart
        st.line_chart(hourly_df["Close"])

    except Exception as e:
        st.error(f"❌ Error fetching or processing data for {pair}: {e}")
