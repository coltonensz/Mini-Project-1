# INF601 - Advanced Programming in Python
# Colton Ensz
# Mini Project 1

import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

data = yf.download("MSFT", start="2022-08-30", end="2022-09-14")

msftPrices = []

for price in data['Adj Close']:
    msftPrices.append(price)

print(msftPrices)

msftarray = np.array(msftPrices)
plt.plot(msftarray)

# show the graph


#plt.savefig('charts/msft.png')
plt.show()
#get ignore /charts



data = yf.download("MSFT", start="2022-08-30", end="2022-09-14")

msftPrices = []

for price in data['Adj Close']:
    msftPrices.append(price)

print(msftPrices)

msftarray = np.array(msftPrices)
plt.plot(msftarray)

# show the graph


#plt.savefig('charts/msft.png')
plt.show()
#get ignore /charts

