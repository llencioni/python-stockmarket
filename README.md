# python-stockmarket

** UNDER DEVELOPMENT ** 


Get stock market information using Python + Qt (HMI)

<img width="500" alt="Screen Shot 2023-10-14 at 14 58 48" src="https://github.com/llencioni/python-stockmarket/assets/44453463/b36efbbd-20f8-436f-92a0-1dfc479e5eb8">

** How to run it:
```
   $ python3 GetStockPrice.py
```

** How to Used It

- Add the tickers you are interested in a .txt file (see an example in the "sample.txt")

- Optionally, select an output file name (.xls)

- Braziliian Ibovespa index should be entered as IBOV


** Notes:

- I used 'pyuic' in the beggining to convert GUI from QtDesigner:
```
pyuic5 -x ./QtDesigner-files/StockMarket.ui -o stockGUI.py
```
- But I've changed the Python code to input the .ui file directly (easier)

- To install all the packages needed to run this code:
```
pip install -r requirements.txt
```
