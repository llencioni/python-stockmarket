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

last_day_stock_info = yf.Ticker(Ticker + ".SA").history("1d")

# Get Stock Price (get rid of index, square brackets, convert array to float)
stock_price = last_day_stock_info['Close']
stock_price = stock_price.values
stock_price = stock_price.astype(str)
stock_price = ''.join(stock_price)
stock_price = float(stock_price)
stock_price = round(stock_price, 2)

# Get Date (convert date to string and get rid of square brackets)
stock_date = last_day_stock_info.index.date
stock_date = stock_date.astype(str)
stock_date = ''.join(stock_date)

# Summary: clousure price and date
print("\n" + Ticker)
print("Date  : " + stock_date)
print("Price : " + str(stock_price))

