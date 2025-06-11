import streamlit as st
from core.data_fetcher import fetch_yahoo
from core.indicators import add_indicators
from core.signal_logic import analyze_pair
from core.tp_sl import calculate_tp_sl

# List of major forex pairs
pairs = ["EURUSD", "GBPUSD", "USDJPY", "USDCHF", "AUDUSD", "USDCAD", "NZDUSD"]

st.title("Forex Prediction Dashboard")

for pair in pairs:
    st.write(f"### {pair}")
    try:
        # Fetch historical data for the pair
        df = fetch_yahoo(pair)
        
        # Add technical indicators (make sure your add_indicators is fixed as discussed)
        df = add_indicators(df)
        
        # Run your signal analysis logic (expects df with indicator columns)
        prediction, confidence = analyze_pair(df)
        
        if prediction is None:
            st.write("Not enough data to generate prediction.")
            continue
        
        latest_price = df["Close"].iloc[-1]
        
        # Calculate Take Profit and Stop Loss levels based on prediction
        tp, sl = calculate_tp_sl(latest_price, prediction)
        
        st.write(f"**Prediction:** {prediction}")
        st.write(f"**Confidence:** {confidence:.1f}%")
        st.write(f"**Take Profit:** {tp:.4f}")
        st.write(f"**Stop Loss:** {sl:.4f}")

    except Exception as e:
        st.error(f"Error fetching or processing data for {pair}: {e}")

