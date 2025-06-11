import streamlit as st
from core.data_fetcher import fetch_yahoo, fetch_alpha_vantage
from core.indicators import add_indicators
from core.signal_logic import analyze_pair
from core.tp_sl import calculate_tp_sl

pairs = ["EURUSD", "GBPUSD", "USDJPY", "USDCHF", "AUDUSD", "USDCAD", "NZDUSD"]

st.title("Forex Prediction Dashboard")

for pair in pairs:
    st.write(f"### {pair}")
    try:
        # Fetch daily data (Yahoo Finance)
        daily_df = fetch_yahoo(pair)
        daily_df = add_indicators(daily_df)
        
        # Fetch hourly/intraday data (Alpha Vantage)
        hourly_df = fetch_alpha_vantage(pair)
        hourly_df = add_indicators(hourly_df)
        
        # Analyze pair with both daily and hourly data
        prediction, confidence = analyze_pair(daily_df, hourly_df)
        
        if prediction is None:
            st.write("Not enough data to generate prediction.")
            continue
        
        latest_price = daily_df["Close"].iloc[-1]
        tp, sl = calculate_tp_sl(latest_price, prediction)
        
        st.write(f"**Prediction:** {prediction}")
        st.write(f"**Confidence:** {confidence:.1f}%")
        st.write(f"**Take Profit:** {tp:.4f}")
        st.write(f"**Stop Loss:** {sl:.4f}")

    except Exception as e:
        st.error(f"Error fetching or processing data for {pair}: {e}")
