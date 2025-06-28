
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
import openpyxl
from openpyxl.styles import Alignment

import sys
import os

######################################
# Get stock prices via Yahoo Finance
######################################
class getStock:
    
    def __init__(self, StocksTicket):
       
        self.FileTxt = StocksTicket
 
        if self.FileTxt:
            print("\nInput .txt with my stock's ticket: " + self.FileTxt)

    def get_stock_price (self):
    
        # Read each line (tickers) and get rid of "\n" in the end of each string
        with open(self.FileTxt,'r') as f:
            Ticker = f.read().splitlines()

        # Name of the Excel file output
        FileName = "MyStocks.xlsx"
        print("Output excel file name: " + FileName)

        # open an excel file
        excel_file = openpyxl.Workbook()
        sheet = excel_file.active
    
        # get stock info
        for i in Ticker:        
    
            if (i == "IBOV"):
                stock_ticker = "^BVSP"
            else:
                stock_ticker = i + ".SA"
            
            last_day_stock_info = yf.Ticker(stock_ticker).history("1d")
            
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
            print("\n" + i)
            print("Date :", stock_date)
            print("Price :", str(stock_price))
            
            # add info in the excel spreedsheet
            sheet.append([i, stock_price, stock_date])
    
        # center align stock price cells
    #    for row in sheet[1:sheet.max_row]:
        #        cell = row[1]
    #        cell.alignment = Alignment(horizontal='center')
    
        # save the excel file
        excel_file.save(FileName)
        
        # open the excel file (only on MacOS)
        if(sys.platform == "darwin"):
            cmd = "open -a '/Applications/Microsoft Excel.app' "+FileName
            os.system(cmd)


# Run this file as script mode (main)
if __name__ == "__main__":

    my_stocks = getStock("MyStocks.txt")

    my_stocks.get_stock_price()
