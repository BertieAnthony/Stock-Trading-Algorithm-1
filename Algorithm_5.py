import yfinance as yf
import pandas as pd
import numpy as np
import statsmodels.api as sm

#This is regression-based forecasting
#I am going to regress the rsi, the sma, and the variance against whether the price went up or down
window = 14
long_window = 25
cash = 10000
shares = 0

apple = yf.download('AAPL', start='2020-01-01', end='2023-01-01')
apple[f"MA{long_window}"] = apple['Close'].rolling(window=long_window).mean()
apple['Change'] = apple['Close'].diff()
apple['Variance'] = apple['Close'].rolling(window=long_window).var()

increase = []
decrease = []
rsis = []
smas = []
variances = []
y = []
counter = 0

for date in apple.index:
    counter += 1
    change = apple['Change'].loc[date]
    ma = float(apple[f"MA{long_window}"].loc[date])
    price = float(apple['Close'].loc[date][-10:])
    variance = float(apple['Variance'].loc[date])
    if pd.notna(ma):
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
        rsis.append(rsi)

        smas.append(ma)
        
        variances.append(variance)

        y.append(1 if change > 0 else 0)

        ycalc = y[1:]
        rsiscalc = rsis[:-1]
        smascalc = smas[:-1]
        variancescalc = variances[:-1]

        X = pd.DataFrame({
            'RSI': rsiscalc,
            'SMA': smascalc,
            'Variance': variancescalc
        })

        X = sm.add_constant(X)
        X = X.dropna()

        if counter >  30:
            model = sm.OLS(ycalc, X)
            results = model.fit()
            prediction = results.predict([1, rsi, ma, variance])[0]
            print(f"Prediction: {prediction}")
            if prediction > 0.5:
                if shares == 0:
                    shares = cash // price
                    cash -= shares * price
            else:
                if shares > 0:
                    cash += shares * price
                    shares = 0
    print(cash, price, shares)
cash = cash + shares * price
print()
print(cash)