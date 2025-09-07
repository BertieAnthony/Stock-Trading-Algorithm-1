# Stock-Trading-Algorithm-1
I am creating multiple simple strock trading algorithms using AAPL data provided by yfinance from 2020-01-01 to 2023-01-01.

Algorithm_1.py is simply a moving average crossover strategy. One is able to control the short run moving average and the long run moving average. Using a short run moving average of 5 days and a long run moving average of 6 days I was able to get a 90.3% return on investment over the 3 years.

Algorithm_3.py is just a bollinger band strategy. You can adjust the length of time over which you calculate the standard deviation and the moving average. Calculating the moving average of 56 days and the standard deviation over 7 days I was able to get an 82.2% return on investment over the 3 years, but this was far more variable depending on what numbers I used to calculate the standard deviation and the length of time for the moving average as small variations in these numbers led to large differences in returns on investment.

Algorithm_2.py is a mix of moving average crossover and a bollinger band strategy. 
It predominantly follows the moving average crossover, but if the price falls above or below x standard deviations of the mean, the bollinger band strategy will kick in and not stop until the price is within one standard deviation of the mean, at which point it will follow the original moving average crossover strategy.
I first tried this strategy with x = 6 and I got a value of 73.3% return which is less than the original moving average crossover strategy. So I decided to get it to run for all values of x between 2 and 19 inclusive, from which I got the results:
[18520.34729385376, 16662.038387298584, 15496.102798461914, 13744.128890991211, 17239.898361206055, 15025.32022857666, 14310.972900390625, 15625.351768493652, 13739.955039978027, 13739.955039978027, 15921.805122375488, 15921.805122375488, 15921.805122375488, 15921.805122375488, 19029.76670074463, 19029.76670074463, 19029.76670074463, 19029.76670074463]
None of these values are greater than the 90.3%, although some are equal because the bollinger bond strategy is never used.
Also what is notable is that none of them are greater than the bollinger band strategy on its own other than using x = 2.
Therefore, I have come to the conclusion that mixing the two strategies makes an overall strategy that is generally weaker than either of its parent strategies.

Algorithm_4.py uses a relative strength index to measure momentum with a moving average filter. You can edit the size of the window to measure the relative strength inex. Using a window size of 14 I was only able to get a 7.6% return on my investment over 3 years, but I attribute this to the fact that I was using apple stock which is unlikely to be particularly over bought or under bought and therefore is unlikely to have large variablity in the relative strength index, which makes it difficult for this algorithm to profit.

Algorithm_5.py uses a regression of RSI, short run moving average, and variance to predict whether the price will increase or decrease. None of these things were particularly good predictors, so during a time when apple stock was decreasing in value, I made a 20% loss. It would work a lot better if I had some more predictive variables.

Algorithm_6.py uses a very simple strategy of if the price increased yesterday then I buy, and if the price decreased yesterday then I sell. From this very simple strategy I was able to get a 52.3% return over the three years.
