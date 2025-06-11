import pandas as pd
import ta

def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    def flatten(series):
        arr = series.to_numpy()
        print(f"Flatten check: original shape={arr.shape}")
        return arr.reshape(-1)

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

    # After all, print shapes of new columns:
    for col in ["MACD", "MACD_signal", "MACD_hist", "RSI", "SMA_20", "SMA_50", "EMA_20", "EMA_50", "BB_upper", "BB_lower"]:
        print(f"Column {col} shape: {df[col].shape}")

    return df
