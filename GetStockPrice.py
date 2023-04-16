# -*- coding: utf-8 -*-

######################################
#
# Get stock prices though Python
#
# By luiz.lencioni@gmail.com
#
######################################

import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import datetime as dt
import yfinance as yf


Ticker = "ITSA4" 

######################################
# Get stock prices via Yahoo Finance
######################################

pega = yf.Ticker(Ticker + ".SA").history("1d")

# We want just the close price
clousure_info = pega['Close']
print("\n")
print(clousure_info)
print("\n")

# Get Stock Price (get rid of index, square brackets, convert array to float)
clousure_info = clousure_info.values
stock_price = clousure_info.astype(str)
stock_price = ''.join(stock_price)
stock_price = float(stock_price)
stock_price = round(stock_price, 2)

# Get Date (convert date to string and get rid of square brackets)
data_cotacao = pega.index.date
stock_date = data_cotacao.astype(str)
stock_date = ''.join(stock_date)

# Summary: clousure price and date
print(Ticker)
print("Date  : " + stock_date)
print("Price : " + str(stock_price))

