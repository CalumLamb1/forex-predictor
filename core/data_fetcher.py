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

    # Debugging output: show keys or error
    print("🔍 API response keys:", data.keys())
    if "Note" in data:
        print("⚠️ API limit hit:", data["Note"])
        return None
    if "Error Message" in data:
        print("❌ API error:", data["Error Message"])
        return None

    if "Time Series FX (60min)" not in data:
        print("❌ 'Time Series FX (60min)' missing from response.")
        return None

    df = pd.DataFrame.from_dict(data["Time Series FX (60min)"], orient="index", dtype=float)
    df.index = pd.to_datetime(df.index)
    df.columns = ["Open", "High", "Low", "Close"]
    df.sort_index(inplace=True)
    return df
