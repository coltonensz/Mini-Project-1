# INF601 - Advanced Programming in Python
# Colton Ensz
# Mini Project 1

import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

data = yf.download("MSFT", start="2022-08-30", end="2022-09-14")


