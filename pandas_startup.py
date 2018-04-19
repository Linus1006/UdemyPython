'''Pandas讀取並處理'''
import pandas as pd

read_csv = pd.read_csv("MI_INDEX.csv", encoding="big5")
df = pd.DataFrame(read_csv)
print(df.tail())

print(read_csv)