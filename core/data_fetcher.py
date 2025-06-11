import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")

def fetch_alpha_vantage(symbol):
    url = f"https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol={symbol[:3]}&to_symbol={symbol[3:]}&interval=60min&apikey={ALPHA_VANTAGE_API_KEY}&outputsize=compact"
    
    response = requests.get(url)
    data = response.json()

    print(f"📡 Raw response for {symbol}:")
    print(data)

    if "Time Series FX (60min)" not in data:
        print(f"❌ Missing 'Time Series FX (60min)' for {symbol}")
        return None

    df = pd.DataFrame.from_dict(data["Time Series FX (60min)"], orient="index", dtype=float)
    df.index = pd.to_datetime(df.index)
    df.columns = ["Open", "High", "Low", "Close"]
    df.sort_index(inplace=True)
    return df
