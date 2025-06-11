import streamlit as st
import json
import numpy as np
from core.data_fetcher import fetch_yahoo
from core.indicators import add_core.indicators
from core.signal_logic import analyze_pair
from core.tp_sl import calculate_tp_sl

st.set_page_config(page_title="Forex Prediction Dashboard", layout="wide")

st.title("📊 Forex Prediction Dashboard")
st.markdown("Shows daily/weekly predictions with confidence, take profit, and stop loss.")

# List of major currency pairs
pairs = ["EURUSD", "GBPUSD", "USDJPY", "USDCHF", "AUDUSD", "USDCAD", "NZDUSD"]

st.sidebar.title("Settings")
selected_source = st.sidebar.selectbox("Data Source", ["Yahoo Finance"])

st.sidebar.markdown("---")
st.sidebar.markdown("✅ Tool uses technical indicators & rule-based logic.")

# Layout
cols = st.columns(3)

for i, pair in enumerate(pairs):
    with cols[i % 3]:
        try:
            # Fetch & prepare data
            if selected_source == "Yahoo Finance":
                hourly = fetch_yahoo(pair)
            else:
                hourly = fetch_alpha_vantage(pair)

            hourly = add_indicators(hourly)

            # ✅ DEBUG: Inspect column shapes
            st.write(f"🔍 Checking column shapes for {pair}")
            for col in hourly.columns:
                arr = hourly[col].dropna().values
                st.write(f"{col}: shape = {arr.shape}, ndim = {arr.ndim}")

            # Analyze the pair
            prediction, confidence = analyze_pair(hourly)

            if prediction is None:
                st.warning(f"{pair}: Not enough data")
                continue

            # TP/SL recommendations
            latest_price = hourly["Close"].iloc[-1]
            tp, sl = calculate_tp_sl(latest_price, prediction)

            st.subheader(pair)
            st.write(f"📈 Prediction: **{prediction}**")
            st.write(f"🔒 Confidence: `{confidence:.1f}%`")
            st.write(f"🎯 Take Profit: `{tp:.4f}`")
            st.write(f"🛑 Stop Loss: `{sl:.4f}`")

        except Exception as e:
            st.error(f"❌ Error fetching or processing data for {pair}: {e}")
            continue
