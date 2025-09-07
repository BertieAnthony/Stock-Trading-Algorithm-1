import yfinance as yf
import pandas as pd
import numpy as np
import time

#This is a very simple strategy where if the stock price inscreased the day before then I will buy
#and if it fell the day before then I will sell.

apple = yf.download('AAPL', start='2020-01-01', end='2023-01-01')
apple['Change'] = apple['Close'].diff()
yesterday = 0
cash = 10000
shares = 0

for date in apple.index:
    change = float(apple['Change'].loc[date])
    price = float(apple['Close'].loc[date])
    if pd.notna(change):
        if change > 0:
            today = 1
        if change < 0:
            today = 0
        if yesterday == 1:
            if shares == 0:
                shares = cash // price
                cash -= shares * price
        if yesterday == 0:
            if shares > 0:
                cash += shares * price
                shares = 0
        yesterday = today
    print(cash, price, shares)
cash = cash + shares * price
print()
print(cash)