import pandas as pd
import ta

def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    if "Close" not in df.columns:
        raise ValueError("Input DataFrame must contain a 'Close' column.")

    def flatten(series):
        return series.to_numpy().reshape(-1)

    df["MACD"] = flatten(ta.trend.macd(df["Close"]))
    df["MACD_signal"] = flatten(ta.trend.macd_signal(df["Close"]))
    df["MACD_hist"] = flatten(ta.trend.macd_diff(df["Close"]))

    df["RSI"] = flatten(ta.momentum.rsi(df["Close"]))

    df["SMA_20"] = flatten(ta.trend.sma_indicator(df["Close"], window=20))
    df["SMA_50"] = flatten(ta.trend.sma_indicator(df["Close"], window=50))

    df["EMA_20"] = flatten(ta.trend.ema_indicator(df["Close"], window=20))
    df["EMA_50"] = flatten(ta.trend.ema_indicator(df["Close"], window=50))

    bb = ta.volatility.BollingerBands(df["Close"], window=20, window_dev=2)
    df["BB_upper"] = flatten(bb.bollinger_hband())
    df["BB_lower"] = flatten(bb.bollinger_lband())

    return df
