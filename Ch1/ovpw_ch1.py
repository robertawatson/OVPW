# Options & Volatility Pricing Workbook
# Chapter 1
# Contract Settlement & Cashflow

import pandas as pd #pylint: disable=E0401
import numpy as np #pylint: disable=E0401

# df = pd.DataFrame(columns = ['Trade Sequence','Stock Price','Trade','Open Position Share','Cash Flow','Cumulative Cash Flow','Realized P&L','Unrealized P&L','Total Cumulative P&L'])
data = pd.read_csv("ch1_data.csv")
w = str("This is a simple calculator for \n Options and Volatility Pricing - Chapter 1 of \n Contract Settlement and Cashflow")
data.head()

def main():
    pass

def welcome():
    print(w)

def calc():
    pass

def readout(): 
    print()
    pass


if __name__ == "__main__":
    main()