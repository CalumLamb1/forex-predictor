import pandas as pd
import ta

def add_indicators(df):
    df = df.copy()
    df["EMA_50"] = ta.trend.ema_indicator(df["Close"].squeeze()
    df["EMA_200"] = ta.trend.ema_indicator(df["Close"].squeeze()
    macd, macd_signal, _ = ta.MACD(df["Close"].squeeze()
df["MACD"] = macd.squeeze()
df["MACD_signal"] = macd_signal.squeeze()
    df["MACD_hist"] = ta.trend.macd_diff(df["Close"].squeeze()
    df["RSI"] = ta.momentum.rsi(df["Close"].squeeze()
    df["ATR"] = ta.volatility.average_true_range(df["High"], df["Low"], df["Close"].squeeze()
    return df
