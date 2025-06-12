import streamlit as st
from core.data_fetcher import fetch_yahoo
from core.indicators import add_indicators
from core.signal_logic import analyze_pair
from core.tp_sl import calculate_tp_sl

st.title("📈 Forex Prediction Dashboard")

# Major pairs
forex_pairs = ["EURUSD", "GBPUSD", "USDJPY", "USDCHF", "AUDUSD", "USDCAD", "NZDUSD"]

for pair in forex_pairs:
    st.subheader(pair)

    try:
        daily_df = fetch_yahoo(pair, interval='1d', period='6mo')
        hourly_df = fetch_yahoo(pair, interval='1h', period='60d')

        daily_df = add_indicators(daily_df)
        hourly_df = add_indicators(hourly_df)

        signal, confidence = analyze_pair(daily_df, hourly_df)
        tp, sl = calculate_tp_sl(hourly_df)

        st.write(f"🔮 Prediction: **{signal}**")
        st.write(f"📊 Confidence: `{confidence}%`")
        st.write(f"🎯 Take Profit: `{tp}`")
        st.write(f"🛡️ Stop Loss: `{sl}`")

        st.line_chart(hourly_df["Close"])

    except Exception as e:
        st.error(f"❌ Error fetching or processing data for {pair}: {e}")
