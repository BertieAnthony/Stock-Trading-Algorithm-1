import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#This is an algorithm using momentum with a moving average filter
#Momentum is calculated using a relative price index

window = 7
long_window = 100
cash = 10000
shares = 0

apple = yf.download('AAPL', start='2020-01-01', end='2023-01-01')
apple[f"MA{long_window}"] = apple['Close'].rolling(window=long_window).mean()
apple['Change'] = apple['Close'].diff()
increase = []
decrease = []

for date in apple.index:
    change = apple['Change'].loc[date]
    ma = float(apple[f"MA{long_window}"].loc[date])
    price = float(apple['Close'].loc[date][-10:])
    if pd.notna(change):
        if change > 0:
            increase.append(change)
            decrease.append(0)
        if change < 0:
            increase.append(0)
            decrease.append(abs(change))
        if len(increase) > window:
            increase.pop(0)
            decrease.pop(0)
        avg_gain = sum(increase) / window
        avg_loss = sum(decrease) / window
        relative_strength = avg_gain / avg_loss if avg_loss != 0 else 0
        rsi = 100 - (100 / (1 + relative_strength)) if avg_loss != 0 else 100
        if rsi < 30 and price > ma:
            if shares == 0:
                shares = cash // price
                cash -= shares * price
        elif rsi > 70 and price < ma:
            if shares > 0:
                cash += shares * price
                shares = 0
    print(cash, price, shares)
cash = cash + shares * price
print()
print(cash)

