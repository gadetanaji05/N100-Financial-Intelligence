import pandas as pd

df = pd.read_excel("data/cashflow.xlsx", header=1)
print(df.columns.tolist())

df = pd.read_excel("data/balancesheet.xlsx", header=1)
print(df.columns.tolist())

df = pd.read_excel("data/profitandloss.xlsx", header=1)
print(df.columns.tolist())