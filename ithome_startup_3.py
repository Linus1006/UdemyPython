'''Day22
import sys as class_info
print(type(class_info))
print(class_info.path)
'''
'''Day23
s = "The {0} {1} tower has {1} floors above ground and five underground".format("Taipei",101)
#print(s)
t = "The {location} {num} tower has {num} floors above ground and five underground".format(location = "Taipei", num = 101)
print(t)
'''
'''Day24 + Day25 + Day26 + Day27
class Human:
    def __init__(self,h = 0, w = 0):
        self.__height = h
        self.__weight = w
    def get_height:
        return self.__height
    def get_weight:
        return self.__weight
    def BMI(self):
        return self.weight / ((self.height/100)**2)
    def __gt__(self, other):
        return self.BMI() > other.BMI()

class Woman(Human):
    def __init__(self,h,w,bust = 0, waist = 0, hip = 0):
        super().__init__(h,w)
        self.bust = bust
        self.waist = waist
        self.hip = hip
    def printBWH(self):
        print("胸圍是{}, 腰圍是{}, 臀圍是{}".format(self.bust,self.waist,self.hip))

#main
mary = Woman(165, 54,83,64,84)
lucy = Woman(180, 70)
print(mary > lucy)
print(lucy > mary)
'''
'''Day29
f = open("news.txt","a")
f.write("abcdkjhkjhjkhjkhjkhkjhjkandcjnsjkngvsjnhfldbnjkadbvhlabdfahljnajlcnjnjlznjkvnafJKnajkdnvjkz")
f.close
f = open("news.txt","r")
print(f.read())
'''
'''Day29 優雅的寫法'''
with open("news.txt","a") as f:
    f.write("abcdkjhkjhjkhjkhjkhkjhjkandcjnsjkngvsjnhfldbnjkadbvhlabdfahljnajlcnjnjlznjkvnafJKnajkdnvjkz")
f = open("news.txt","r")
print(f.read())
