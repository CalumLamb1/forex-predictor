import yfinance as yf

def fetch_yahoo(pair, interval='1d', period='3mo'):
    ticker = pair + "=X"
    df = yf.download(ticker, interval=interval, period=period)
    df.dropna(inplace=True)
    df.reset_index(inplace=True)
    return df
