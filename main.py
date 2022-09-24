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
plt.title("MSFT")

# show the graph

plt.savefig('charts/msft.png')
plt.show()


#Create AAPL chart
dataAAPL = yf.download("AAPL", start="2022-08-30", end="2022-09-14")

AAPLPrices = []

for price in dataAAPL['Adj Close']:
    AAPLPrices.append(price)

print(AAPLPrices)

AAPLarray = np.array(AAPLPrices)
plt.plot(AAPLarray)
plt.title("AAPL")

# show the graph


plt.savefig('charts/aapl.png')
plt.show()


