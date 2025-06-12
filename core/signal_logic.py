def analyze_pair(daily_df, hourly_df):
    # Simple rule-based prediction
    last_rsi = hourly_df["RSI"].iloc[-1]
    last_macd = hourly_df["MACD"].iloc[-1]
    last_macd_signal = hourly_df["MACD_Signal"].iloc[-1]

    if last_rsi < 30 and last_macd > last_macd_signal:
        return "BUY", 0.85
    elif last_rsi > 70 and last_macd < last_macd_signal:
        return "SELL", 0.85
    else:
        return "HOLD", 0.5
