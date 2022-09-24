# INF601 - Advanced Programming in Python
# Colton Ensz
# Mini Project 1

from tkinter import W
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

aaplPrices = []

for price in dataAAPL['Adj Close']:
    aaplPrices.append(price)

print(aaplPrices)

aaplarray = np.array(aaplPrices)
plt.plot(aaplarray)
plt.title("AAPL")

# show the graph


plt.savefig('charts/aapl.png')
plt.show()

#Create TSLA chart
dataTSLA = yf.download("TSLA", start="2022-08-30", end="2022-09-14")

TSLAPrices = []

for price in dataTSLA['Adj Close']:
    TSLAPrices.append(price)

print(TSLAPrices)

TSLAarray = np.array(TSLAPrices)
plt.plot(TSLAarray)
plt.title("TSLA")

# show the graph


plt.savefig('charts/tsla.png')
plt.show()

#Create MCD chart
datamcd = yf.download("MCD", start="2022-08-30", end="2022-09-14")

mcdPrices = []

for price in datamcd['Adj Close']:
    mcdPrices.append(price)

print(mcdPrices)

mcdarray = np.array(mcdPrices)
plt.plot(mcdarray)
plt.title("MCD")

# show the graph


plt.savefig('charts/mcd.png')
plt.show()


#Create WMT chart
datawmt = yf.download("WMT", start="2022-08-30", end="2022-09-14")

wmtPrices = []

for price in datawmt['Adj Close']:
    wmtPrices.append(price)

print(wmtPrices)

wmtarray = np.array(wmtPrices)
plt.plot(wmtarray)
plt.title("WMT")

# show the graph


plt.savefig('charts/wmt.png')
plt.show()

