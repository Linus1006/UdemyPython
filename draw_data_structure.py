'''tuple
tp=()
print(tp)
tp2=(1,2,3,4,5,6,7,8)
print(tp2)
print(sum(tp2))
print(tp2[2:5])
print(tp2[-1])
tp6=tuple([1,2,3,4,5,6,7,8,0])
print(tp6)
list1=list(tp6)
list2 = sorted(list1,reverse=True)
print(list1)
print(list2)
'''
'''Set
st1=set()#建立一個空集合
st2=set([1,2,3,4,5])
print(st2)
st3={'a','b','c','d','e'}
print(st3)
print('-------------------')
st3.add('f')
print(st3)
st3.remove('d')
print(st3)
print('----------')
print(st3.union(st2))
st5={'a','b','c','d','e'}
print(st3.intersection(st5))
print(st3.difference(st5))
'''
'''scipy linalg
import numpy as np
from scipy import linalg as linear

A = np.array([[1,3,5], [2,5,1], [2,3,8]])
print(A)
A_inv = linear.inv(A)
print(A_inv)
print(np.matmul(A,A_inv))
print(A.dot(A_inv))

B = np.array([[1,2],[3,4]])
print(linear.det(B))
'''
'''numpy模組建立矩陣
import numpy as np
my_array = np.array([[1,2,3],[4,5,6]])
print(my_array)
my_zero = np.zeros((3,5), dtype = np.int16)
print(my_zero)

my_onedim_arr = np.arange(15, dtype = np.int64)
print(my_onedim_arr)
#矩陣轉換形狀
my_reshape_arr = my_onedim_arr.reshape((15,1))
print(my_reshape_arr)
#矩陣切片
my_slice_arr = np.linspace(1,100,8) #切7等分
print(my_slice_arr)
#建立0~1隨機2*3矩陣
my_random_arr = np.random.random((10,10))
print(my_random_arr)
#矩陣運算
a = np.arange(25).reshape((5,5))
b = np.random.random((5,5))
print(a)
print(b)
print("a+b",a+b)
print("a-b:",a-b)
print("a*b:",a*b)
print("a.b:",a.dot(b))
'''
'''#sin函數計算並畫圖
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 3*np.pi, 0.011)
y = np.sin(x)
#plt.plot(x, y)

mu = 2
sigma = 0.5
v = np.random.normal(mu, sigma, 10000)
plt.hist(v, bins=500, normed=1)
plt.show()
'''
'''輸入並更改矩陣維度
import numpy as np
a_10_3= np.zeros((10,3))
print(a_10_3)
a_3_10 = a_10_3.T
print(a_10_3)
b_5_6 = np.reshape(a_10_3,(5,6))
print(b_5_6)
c_5_1 = np.ravel(b_5_6)
print(c_5_1)
'''
