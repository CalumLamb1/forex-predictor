import yfinance as yf

def fetch_yahoo(ticker, period='6mo', interval='1d'):
    df = yf.download(ticker, period=period, interval=interval)
    df.dropna(inplace=True)
    return df
