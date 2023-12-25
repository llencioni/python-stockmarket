# python-stockmarket

*** UNDER DEVELOPMENT *** 


Get stock market information using Python + Qt (HMI)

<img width="500" alt="Screen Shot 2023-10-14 at 14 58 48" src="https://github.com/llencioni/python-stockmarket/assets/44453463/b36efbbd-20f8-436f-92a0-1dfc479e5eb8">


# Use Case requirements (TBC)

![Use-cases-stockInfo](https://github.com/llencioni/python-stockmarket/assets/44453463/b95e1ee4-1e2e-4d1a-a4c2-2d6e656a0017)

** diagram created in PlantUML


## How to run it:
```console
python3 main.py
```

## How to Used it:

- Add the tickers you are interested in a .txt file (see an example in the "sample.txt")

- Optionally, select an output file name (.xls)

- Braziliian Ibovespa index should be entered as IBOV


## Design Notes:

- I used 'pyuic' in the beggining to convert GUI from QtDesigner:
```console
pyuic5 -x ./QtDesigner-files/StockMarket.ui -o stockGUI.py
```
- But I've changed the Python code to input the .ui file directly (easier)
```py
uic.loadUi("./QtDesigner-files/StockMarket.ui", self)
```
- To install all the packages needed to run this code:
```console
pip install -r requirements.txt
```

## References

Plant UML tool

https://plantuml.com

