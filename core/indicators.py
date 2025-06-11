import ta

def add_indicators(df):
    # Simple Moving Average and Exponential Moving Average
    df["SMA_20"] = df["Close"].rolling(window=20).mean()
    df["EMA_20"] = df["Close"].ewm(span=20).mean()

    # RSI - flatten output to 1D array
    df["RSI"] = ta.momentum.rsi(df["Close"], window=14).values.flatten()

    # MACD components - flatten all to 1D
    df["MACD"] = ta.trend.macd(df["Close"]).values.flatten()
    df["MACD_signal"] = ta.trend.macd_signal(df["Close"]).values.flatten()
    df["MACD_hist"] = ta.trend.macd_diff(df["Close"]).values.flatten()

    # ATR - flatten output to 1D
    df["ATR"] = ta.volatility.average_true_range(
        high=df["High"], low=df["Low"], close=df["Close"], window=14
    ).values.flatten()

    return df
