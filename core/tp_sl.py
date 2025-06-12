def calculate_tp_sl(df):
    last_price = df["Close"].iloc[-1]

    # Simple fixed % strategy
    take_profit = last_price * 1.005  # +0.5%
    stop_loss = last_price * 0.995    # -0.5%

    return take_profit, stop_loss
