import streamlit as st
import json
from core.data_fetcher import fetch_yahoo, fetch_alpha_vantage
from core.indicators import add_indicators
from core.signal_logic import analyze_pair
from core.tp_sl import calculate_tp_sl

# Title and description
st.set_page_config(page_title="Forex Predictor", layout="wide")
st.title("💹 Forex Market Predictor Dashboard")
st.markdown("This tool uses trend analysis + heuristics to generate trade signals for major Forex pairs.")

# Load currency pairs
with open("assets/pair_list.json") as f:
    pairs = json.load(f)
    pairs = ["EURUSD"]  # Temporary override for testing


# Choose data source
source = "Yahoo Finance"

results = []

with st.spinner("Fetching and analyzing data..."):
    for pair in pairs:
        try:
            if source == "Yahoo Finance":
                daily = fetch_yahoo(pair, interval="1d", period="6mo")
                hourly = fetch_yahoo(pair, interval="1h", period="7d")
            else:
                daily = fetch_yahoo(pair, interval="1d", period="6mo")  # still use Yahoo for daily
                hourly = fetch_alpha_vantage(pair, interval="60min")

            daily = add_indicators(daily)
            hourly = add_indicators(hourly)
            import numpy as np
st.write(f"🔍 Checking column shapes for {pair}")
for col in hourly.columns:
    arr = hourly[col].dropna().values
    st.write(f"{col}: shape={arr.shape}, ndim={arr.ndim}")

    except Exception as e:
    st.error(f"❌ Error fetching or processing data for {pair}: {e}")
    continue


            result = analyze_pair(pair, daily, hourly)
            latest_close = hourly["Close"].iloc[-1]
            atr = daily["ATR"].iloc[-1]
            tp, sl = calculate_tp_sl(latest_close, result["direction"], atr)

            result.update({
                "current_price": round(latest_close, 5),
                "tp": tp,
                "sl": sl
            })

            results.append(result)

        except Exception as e:
            st.warning(f"Error fetching data for {pair}: {e}")

# Display results
if results:
    df = (
        st.dataframe(
            {k: [r[k] for r in results] for k in results[0]},
            use_container_width=True
        )
    )
else:
    st.error("No results available. Please check your API key or data source.")

# Optional: Add filters or notifications in future versions
