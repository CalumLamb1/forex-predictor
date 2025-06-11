import pandas as pd
import ta  # Make sure 'ta' is installed

def add_indicators(df):
    # Moving Averages
    df["SMA_20"] = df["Close"].rolling(window=20).mean()
    df["EMA_20"] = df["Close"].ewm(span=20).mean()
    
    # RSI
    df["RSI"] = ta.momentum.rsi(df["Close"], window=14)

    # MACD
    df["MACD"] = ta.trend.macd(df["Close"]).squeeze()
    df["MACD_signal"] = ta.trend.macd_signal(df["Close"]).squeeze()
    df["MACD_hist"] = ta.trend.macd_diff(df["Close"]).squeeze()

    # ATR
    df["ATR"] = ta.volatility.average_true_range(
        high=df["High"], low=df["Low"], close=df["Close"], window=14
    )

    return df

