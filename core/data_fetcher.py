import os
import yfinance as yf
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

AV_KEY = os.getenv("ALPHA_VANTAGE_KEY")
AV_URL = "https://www.alphavantage.co/query"

def fetch_yahoo(pair, interval="1d", period="1y"):
    ticker = pair + "=X"
    df = yf.download(ticker, period=period, interval=interval)
    df = df.rename(columns={"Volume":"Volume"})
    return df

def fetch_alpha_vantage(pair, interval="60min"):
    params = {
        "function": "FX_INTRADAY",
        "from_symbol": pair[:3],
        "to_symbol": pair[3:],
        "interval": interval,
        "apikey": AV_KEY,
        "outputsize": "compact"
    }
    r = requests.get(AV_URL, params=params)
    data = r.json()
    key = f"Time Series FX ({interval})"
    df = pd.DataFrame.from_dict(data[key], orient="index")
    df = df.rename(columns={
        "1. open":"Open","2. high":"High","3. low":"Low",
        "4. close":"Close"
    }).astype(float)
    df.index = pd.to_datetime(df.index)
    df.sort_index(inplace=True)
    return df
