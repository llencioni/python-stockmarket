# python-stockmarket

** UNDER DEVELOPMENT ** 


Get stock market information using Python + Qt (HMI)

<img width="500" alt="Screen Shot 2023-10-14 at 14 58 48" src="https://github.com/llencioni/python-stockmarket/assets/44453463/b36efbbd-20f8-436f-92a0-1dfc479e5eb8">

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
