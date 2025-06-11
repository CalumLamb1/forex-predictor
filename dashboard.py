import streamlit as st
from core.data_fetcher import fetch_yahoo
from core.indicators import add_indicators
from core.signal_logic import analyze_pair
from core.tp_sl import calculate_tp_sl

pairs = ["EURUSD", "GBPUSD", "USDJPY", "USDCHF", "AUDUSD", "USDCAD", "NZDUSD"]

st.title("Forex Prediction Dashboard")

for pair in pairs:
    try:
        # Fetch data
        df = fetch_yahoo(pair)
        
        # Add technical indicators
        df = add_indicators(df)
        
        # Run your analysis function which expects 1D Series inside df columns
        prediction, confidence = analyze_pair(df)
        
        if prediction is None:
            st.write(f"{pair}: Not enough data to predict")
            continue
        
        latest_price = df["Close"].iloc[-1]
        tp, sl = calculate_tp_sl(latest_price, prediction)
        
        st.subheader(pair)
        st.write(f"Prediction: {prediction}")
        st.write(f"Confidence: {confidence:.1f}%")
        st.write(f"Take Profit: {tp:.4f}")
        st.write(f"Stop Loss: {sl:.4f}")
        
    except Exception as e:
        st.error(f"Error fetching or processing {pair}: {e}")
