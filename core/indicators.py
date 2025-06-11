import pandas as pd
import ta  # Technical Analysis library


def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    # Ensure 'Close' column exists
    if "Close" not in df.columns:
        raise ValueError("Input DataFrame must contain a 'Close' column.")

    # MACD indicators
    df["MACD"] = ta.trend.macd(df["Close"]).to_numpy().reshape(-1)
    df["MACD_signal"] = ta.trend.macd_signal(df["Close"]).to_numpy().reshape(-1)
    df["MACD_hist"] = ta.trend.macd_diff(df["Close"]).to_numpy().reshape(-1)

    # RSI (Relative Strength Index)
    df["RSI"] = ta.momentum.rsi(df["Close"]).to_numpy().reshape(-1)

    # Simple Moving Averages (SMA)
    df["SMA_20"] = ta.trend.sma_indicator(df["Close"], window=20).to_numpy().reshape(-1)
    df["SMA_50"] = ta.trend.sma_indicator(df]()
