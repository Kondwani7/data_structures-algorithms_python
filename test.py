import sys


num = [3, 2, 4, 5, 7 ,6]
print(num[num[2]])
#print(list[-2:])
#print(int(123))
from sys import getsizeof
#print(sys.maxsize)
#print(float(.1))
s = getsizeof(int)
#print(s)
nums = [5, 2, 4]
def sqsum4():
  	return sum(x**2 for x in nums if x > 0)

#print(sqsum4())
class FunEvent:
    def __init__(self, tags, year):
        self.tags = tags
        self.year = year
    
    def __str__(self):
        return f"FunEvent(tags={self.tags}, year={self.year})"

tags = ["google", "ml"]
year = 2022
bootcamp = FunEvent(tags, year)
tags.append("bootcamp")
year = 2023
#print(bootcamp)

class BaseLayer:
    def __init__(self, name=""):
        self.name = name

    def __repr__(self):
        return f"{self.name}Layer"

class ActivationLayer(BaseLayer):
    def __init__(self, size):
        super().__init__("Activation")
        self.size = size

class FCLayer(BaseLayer):
    def __init__(self, size):
        super().__init__("FullyConnected")
        self.size = size

#print(FCLayer(42))
a = BaseLayer("hey")
b = ActivationLayer(23)
#print(a.name)
#print(b.size)

def f1(list_of_list):
    result = []
    for inner_list in list_of_list:
        for x in inner_list:
            if x not in result:
                result.append(x)
    return result

def f2(list_of_list):
    flat_list = []
    for inner_list in list_of_list:
        flat_list.extend(inner_list)
    return [
        x for i, x in enumerate(flat_list)
        if flat_list.index(x) == i]

def f3(list_of_list):
    result = []
    seen = set()
    for inner_list in list_of_list:
        for x in inner_list:
            if x not in seen:
                result.append(x)
                seen.add(x)
    return result

x = [[3], [2, 2], [3, 4, 5]]
#print(f3(x))
#print(f1(x))
#print(f2(x))