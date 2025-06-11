import streamlit as st
from core.data_fetcher import fetch_yahoo  # or fetch_alpha_vantage if you implement that
from core.indicators import add_indicators
from core.signal_logic import analyze_pair
from core.tp_sl import calculate_tp_sl

st.set_page_config(page_title="Forex Prediction Dashboard", layout="wide")

st.title("📊 Forex Prediction Dashboard")
st.markdown("Daily/Weekly predictions with confidence, take profit, and stop loss.")

pairs = ["EURUSD", "GBPUSD", "USDJPY", "USDCHF", "AUDUSD", "USDCAD", "NZDUSD"]

st.sidebar.title("Settings")
selected_source = st.sidebar.selectbox("Data Source", ["Yahoo Finance"])

cols = st.columns(3)

for i, pair in enumerate(pairs):
    with cols[i % 3]:
        try:
            # Fetch and prepare data
            if selected_source == "Yahoo Finance":
                df = fetch_yahoo(pair)
            else:
                # Placeholder for other sources
                df = fetch_alpha_vantage(pair)

            df = add_indicators(df)

            # Debug: check shapes of columns
            st.write(f"🔍 Checking column shapes for {pair}")
            for col in df.columns:
                arr = df[col].dropna().values
                st.write(f"{col}: shape = {arr.shape}, ndim = {arr.ndim}")

            # Analyze pair prediction
            prediction, confidence = analyze_pair(df)

            if prediction is None:
                st.warning(f"{pair}: Not enough data to predict")
                continue

            latest_price = df["Close"].iloc[-1]
            tp, sl = calculate_tp_sl(latest_price, prediction)

            st.subheader(pair)
            st.write(f"📈 Prediction: **{prediction}**")
            st.write(f"🔒 Confidence: `{confidence:.1f}%`")
            st.write(f"🎯 Take Profit: `{tp:.4f}`")
            st.write(f"🛑 Stop Loss: `{sl:.4f}`")

        except Exception as e:
            st.error(f"❌ Error fetching or processing data for {pair}: {e}")
            continue
