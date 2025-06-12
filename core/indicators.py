import pandas as pd
import ta  # Make sure 'ta' is installed: pip install ta

def add_indicators(df):
    df = df.copy()

    # Ensure 'Close' column exists and is 1D
    df["Close"] = df["Close"].astype(float)

    # Add SMA
    df["SMA_50"] = ta.trend.sma_indicator(df["Close"], window=50)
    df["SMA_200"] = ta.trend.sma_indicator(df["Close"], window=200)

    # Add RSI
    df["RSI"] = ta.momentum.RSIIndicator(df["Close"], window=14).rsi()

    # Add MACD
    macd = ta.trend.MACD(df["Close"])
    df["MACD"] = macd.macd()
    df["MACD_Signal"] = macd.macd_signal()
    df["MACD_Hist"] = macd.macd_diff()

    df.dropna(inplace=True)
    return df
