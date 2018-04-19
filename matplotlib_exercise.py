'''用matplotlib繪圖
import matplotlib.pyplot as mpt

month1 = [1,2,3,4,5,8,10,12]
month2 = [1,3,4,5,6,7,11,12]
sales1 = [20000,40000,60000,80000,100000,120000,140000,160000]
sales2 = [10000,20000,30000,150000,120000,80000,60000,210000]

mpt.plot(month1,sales1, lw = 2, label = "Mimian")
mpt.plot(month2,sales2, lw = 2, label = "Linus")
mpt.xlabel("Month")
mpt.ylabel("dollar")
mpt.legend()
mpt.title('matplotlib_example')
mpt.show()
'''
'''小練習
import matplotlib.pyplot as mpt

mpt.plot([1,2,3,4,5],[55,25,35,41,12],'ro')
mpt.ylabel("輸入為y軸")
mpt.axis([0,6,0,60])
mpt.show()
'''
'''進階小練習'''
import matplotlib.pyplot as mpt
import numpy as np

aranges = np.arange(0,5,0.2)
mpt.plot(aranges,aranges,"r--",aranges,aranges**2,"bs",aranges,aranges**3,"g^")
mpt.show()


