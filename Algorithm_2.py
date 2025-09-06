import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#This is a mix of a bollinger band stratey and a moving average crossover strategy
#It is predominantly going to follow the moving average crossover strategy,
#but if the price goes below x standard deviations of the long run average then it will buy shares.
#It will only sell these shares once the price goes within 1 sd of the long run average.
#Then it will follow the moving average crossover strategy again.
#Unless it goes above x standard deviation of the long run average, 
#then it will sell all shares and wait until the price goes within 1sd of the long run average.

short_window = 5
long_window = 26
standard_deviation = 7

totals = []

for x in range(2, 20):
    apple = yf.download('AAPL', start='2020-01-01', end='2023-01-01')
    apple[f"MA{short_window}"] = apple['Close'].rolling(window=short_window).mean()
    apple[f"MA{long_window}"] = apple['Close'].rolling(window=long_window).mean()
    apple[f"STD{standard_deviation}"] = apple['Close'].rolling(window=standard_deviation).std()


    yesterday = 0
    cash = 10000
    shares = 0
    bollinger = 0 #This tests whether it is in above or below the bollinger bands

    if shares == 0:
        for date in apple.index:
            mashort = apple[f"MA{short_window}"].loc[date]
            malong = apple[f"MA{long_window}"].loc[date]
            price = apple['Close'].loc[date][-10:]
            sd = float(apple[f"STD{standard_deviation}"].loc[date])
            if pd.notna(mashort) and pd.notna(malong):
                price = float(price)
                mashort = float(mashort)
                malong = float(malong)
                if price > malong + x * sd:
                    if bollinger < 1:
                        bollinger = 1
                        cash += shares * price
                        shares = 0
                elif price < malong - x * sd:
                    if bollinger > -1:
                        bollinger = -1
                        shares = cash // price
                        cash -= shares * price
                if mashort > malong:
                    today = 1
                if mashort < malong:
                    today = 0
                if bollinger == 1:
                    if price < malong + sd:
                        bollinger = 0
                if bollinger == -1:
                    if price > malong - sd:
                        bollinger = 0
                        cash += shares * price
                        shares = 0
                if bollinger == 0:
                    if today > yesterday:
                        shares = cash // price
                        cash -= shares * price
                    if today < yesterday:
                        cash += shares * price
                        shares = 0
                yesterday = today
            print(cash, price, shares)
            
        cash = cash + shares * price
        print()
        print(cash)
        totals.append(cash)
print()
print()
print()
print(totals)