'''Pandas讀取並處理'''
import pandas as pd
'''
names = ["小寶","小文","阿呆","John","Lin"]
my_array = pd.Series(names)
print(my_array)

SalarysDic = {"John":"50000", "lvy":"90000", "Mary":"20000", "Steven":"35000", "David":"85000" }
myDic = pd.Series(SalarysDic, index=SalarysDic.keys())
print(myDic)
print("0 1 3:",myDic[[0,1,3]])
print("Mary:",myDic["Mary"])
'''
read_csv = pd.read_csv("MI_INDEX.csv", encoding="big5")
df = pd.DataFrame(read_csv)
#print(read_csv)
#print(df.info)
print(df.columns)

groups = ["Movies", "Sports", "Coding", "Fishing", "Dancing", "cooking"]  
num = [46, 8, 12, 12, 6, 58]

dict = {"groups": groups,  
        "num": num
       }

select_df = pd.DataFrame(dict)
print(select_df.iloc[:,:])      #所有資料
print(select_df.iloc[0, 1])     # 第一列第二欄：組的人數  
print("---")  
print(select_df.iloc[0:1,:])    # 第一列：組的組名與人數  
print("---")  
print(select_df.iloc[:,1])      # 第二欄：各組的人數  
print("---")  
print(select_df["num"])         # 各組的人數  
print("---")  
print(select_df.num)    # 各組的人數 