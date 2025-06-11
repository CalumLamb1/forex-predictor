def calculate_tp_sl(entry, direction, atr):
    if direction == "Buy":
        sl = entry - 1.5 * atr
        tp = entry + 3.0 * atr
    else:
        sl = entry + 1.5 * atr
        tp = entry - 3.0 * atr
    return round(tp, 5), round(sl, 5)
