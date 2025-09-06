# Stock-Trading-Algorithm-1
I am creating multiple simple strock trading algorithms using AAPL data provided by yfinance from 2020-01-01 to 2023-01-01.

Algorithm_1.py is simply a moving average crossover strategy. One is able to control the short run moving average and the long run moving average. Using a short run moving average of 5 days and a long run moving average of 6 days I was able to get a 90.3% return on investment over the 3 years.

Algorithm_3.py is just a bollinger band strategy. You can adjust the length of time over which you calculate the standard deviation and the moving average. Calculating the moving average of 56 days and the standard deviation over 7 days I was able to get an 82.2% return on investment over the 3 years, but this was far more variable depending on what numbers I used to calculate the standard deviation and the length of time for the moving average as small variations in these numbers led to large differences in returns on investment.
