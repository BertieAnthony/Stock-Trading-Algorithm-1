import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#This is a simple bollinger band strategy
apple = yf.download('AAPL', start='2020-01-01', end='2023-01-01')
apple['MA'] = apple['Close'].rolling(window=50).mean()
apple['STD'] = apple['Close'].rolling(window=20).std()

cash = 10000
shares = 0
bollinger = 0

for date in apple.index:
    ma = apple['MA'].loc[date]
    price = apple['Close'].loc[date]
    sd = float(apple['STD'].loc[date])
    if pd.notna(ma):
        ma = float(ma)
        price = float(price)
        if price > ma + sd * 2:
            if bollinger < 1:
                bollinger = 1
                cash += shares * price
                shares = 0
        elif price < ma - sd * 2:
            if bollinger > -1:
                bollinger = -1
                shares = cash // price
                cash -= shares * price
    print(cash, price, shares, 2*sd + ma, ma - 2*sd)
cash = cash + shares * price
print()
print(cash)    
