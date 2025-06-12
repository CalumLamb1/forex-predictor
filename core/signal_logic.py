def analyze_pair(df):
    latest = df.iloc[-1]

    signal = "❓ No clear signal"

    if latest["SMA_50"] > latest["SMA_200"] and latest["RSI"] < 70:
        signal = "📈 Buy Signal"
    elif latest["SMA_50"] < latest["SMA_200"] and latest["RSI"] > 30:
        signal = "📉 Sell Signal"

    return signal
