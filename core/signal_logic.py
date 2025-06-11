import numpy as np

def confidence_score(daily, hourly):
    score = 0
    if daily["EMA_50"].iloc[-1] > daily["EMA_200"].iloc[-1]:
        score += 30
    if daily["MACD_hist"].iloc[-1] > 0:
        score += 20
    if hourly["Close"].iloc[-1] > hourly["EMA_50"].iloc[-1]:
        score += 25
    if hourly["MACD_hist"].iloc[-1] > 0:
        score += 15
    vol_trend = daily["Volume"].diff().tail(3).sum()
    price_trend = daily["Close"].diff().tail(3).sum()
    if price_trend * vol_trend > 0:
        score += 10
    return np.clip(score, 0, 100)

def analyze_pair(pair, daily_df, hourly_df):
    daily = daily_df.copy().dropna()
    hourly = hourly_df.copy().dropna()
    score = confidence_score(daily, hourly)
    direction = "Buy" if (daily["EMA_50"].iloc[-1] > daily["EMA_200"].iloc[-1]) else "Sell"
    return {"pair":pair, "direction":direction, "confidence":score}
