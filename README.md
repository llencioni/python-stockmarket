# python-stockmarket
Get stock market information using Python + Qt (HMI)

To install all the packages needed to run this code:
>> pip install -r requirements.txt

** How to Used It

. Put the tickers you are interested in a .txt file (see examaple in the "sample.txt")

. Optionally, select an output file name (.xls)

. Braziliian Ibovespa index should be entered as IBOV


** Notes:

. I used to convert GUI from QtDesigner using 'pyuic':
>> pyuic5 -x ./QtDesigner-files/StockMarket.ui -o stockGUI.py

. But now I've changed the code to input the .ui file directly (easier)
