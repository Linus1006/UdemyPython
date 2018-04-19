
''' Day 7
i = 1
ans = 0

while i<=15:
    if ans%3 ==0 :
        print(ans,"是3的倍數")
    ans +=2
    i += 1

while True:
    str = input("請輸入結束")
    if str == 'p':
        break
    else:
        print("繼續GO")
'''

'''Day8
numbers = range(0,16,2)
ans = 0
for number in numbers:
    ans = ans + number
    
print(ans)

text = "taipei city"
for letter in text:
    print(letter, " \n")
'''
'''Day9
def max(a, b):
    if a > b:
        return a
    else:
        return b

print("Max:",max(10,20))

def max_in_list(*a):
    top = 0
    for number in a:
        if(number > top):
            top = number
    return top

print("Top:",max_in_list(10,11,14,55,64,33,1))
'''
'''Day 10
#tuple 
location = ("taipei", 101, "信義區")
#print(location[0])
#print(location[1])

location = location + ("市政府",)
print(location)
location_copy = location * 3
print(location_copy)
'''
'''Day11'''
a = 1
b = 999
a,b = b,a #(a ,b) = (b,a)
print("a:" ,a , "b:",b )

for x,y,z in ((1,2,3), (3,4,5), (5,6,7)):
    print(x+y+z)
'''Day 17'''
a = lambda x:x*x
b = lambda x,y,z : (x+y+z)/2
c = lambda i,o,p : "hello " + i + ", ans = " + str(o+p)
print(a(3)) 
print(b(3,4,5))
print(c("Linus",7,3))
