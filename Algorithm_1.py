import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

short_window = 5
long_window = 26

apple = yf.download('AAPL', start='2020-01-01', end='2023-01-01')
apple[f"MA{short_window}"] = apple['Close'].rolling(window=short_window).mean()
apple[f"MA{long_window}"] = apple['Close'].rolling(window=long_window).mean()

yesterday = 0
cash = 10000
shares = 0

if shares == 0:
    for date in apple.index:
        mashort = apple[f"MA{short_window}"].loc[date]
        malong = apple[f"MA{long_window}"].loc[date]
        price = apple['Close'].loc[date][-10:]
        if pd.notna(mashort) and pd.notna(malong):
            if mashort > malong:
                today = 1
            if mashort < malong:
                today = 0
            if today > yesterday:
                shares = 50
                cash -= shares * price
            if today < yesterday:
                cash += shares * price
                shares = 0
            yesterday = today
        print(price)
        
    cash = cash + shares * price
    print()
    print(cash)    

