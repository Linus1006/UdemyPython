import pandas as pd
import numpy as np

df1 = pd.DataFrame( np.random.randn(6,4), index=list('abcdef'), columns=list('ABCD'))
print(df1)

print( df1.loc[lambda n: n.A >1 ,:])    #印出有大於1的列

print(df1.loc[:, lambda n: ["A","B"]])  #第A及B欄

print(df1.iloc[:,lambda n:[0, 1]])      #第0與1欄

