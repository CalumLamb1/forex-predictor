import pandas as pd
import ta

def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    # Ensure 'Close' is a Series, not DataFrame
    close = df["Close"]
    if isinstance(close, pd.DataFrame):
        close = close.squeeze()  # convert to Series if needed

    df["MACD"] = ta.trend.macd(close)
    df["MACD_signal"] = ta.trend.macd_signal(close)
    df["MACD_hist"] = ta.trend.macd_diff(close)

    df["RSI"] = ta.momentum.rsi(close)

    df["SMA_20"] = ta.trend.sma_indicator(close, window=20)
    df["SMA_50"] = ta.trend.sma_indicator(close, window=50)

    df["EMA_20"] = ta.trend.ema_indicator(close, window=20)
    df["EMA_50"] = ta.trend.ema_indicator(close, window=50)

    bb = ta.volatility.BollingerBands(close, window=20, window_dev=2)
    df["BB_upper"] = bb.bollinger_hband()
    df["BB_lower"] = bb.bollinger_lband()

    return df
