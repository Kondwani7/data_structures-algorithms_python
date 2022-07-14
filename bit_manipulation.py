"""

#base2 - a sequence of 1s and 0s
#operateors:
#Bitwise AND (&)OR (|), XOR(^),NOT(!) XOR()
"""
#functions get a bit
from os import GRND_RANDOM


def getBit(num , i):
    #finds a bit of any given number And -> 1 << i
    return ((num & (1 << i)) != 0)
#set a bit in a particular position
def setBit(num, i):
    #or operation 
    return num | (1<< i)
#clear a bit
#~(1<<i) unset it \
def clearBit(num, i):
    #create a mask for the ith
    #bit unset
    mask = ~(1  << i)
    #return our udpdated value
    return num & mask
#implementation
N = 21
print("The bit at 3rd position :", 1 if (getBit(N, 3)) else 0 )
print("the value of our number changes after setting the bit to:", setBit(N, 0))
print("The value of our number changes after clearing the bit to:", clearBit(N, 0))
#base 2 for example
#in decimal 1234  in base 10 is 
print("1234 in base 10:", (1 * 10**3 + 2 * 10**2 + 3 * 10 **1 + 4 * 10 ** 0 ))
#base 2, binary we go from right to left 
#e.g 13
print("1011 in base 2:", (1 * 2 ** 0 + 0 * 2**1 + 1 * 2 ** 2 + 1 * 2 ** 3))
#e.g
x = 0b110010110
y = 0b10101101
#ob - start binary
#remember start from right to left so for z read like: 
# 1 * (2^0) + 0 * (2^1) + 1 * (2^2) + 0 *  (2^3) + 1 *  (2^4) + 0 * (2^5) + 1 * (2^6) 
# + 0 * (2^7) + 1 * (2^8)
z = 0b101010101
print(x)
print(y)
print("base: 0b101010101 -> ", z)
#compares both numbers x if there is 1 on both then : 1 else 0
#x -> 0b110010110
#z -> 0b101010101
#x & z
#ans: 0b100010100 -> 0 *(2^0) + 0 *(2^1) + 1 *(2^2) + 0 *(2^3) + 1 *(2^4)
# 0 *(2^5) + 0 *(2^6) + 0 *(2^7) + 1 *(2^8)
# x & z if both are 1 then 1 else 0  
print("the AND operator of x & z(276):", (x & z))
# OR |
#x -> 0b110010110
#z -> 0b101010101
#ans: 0b111010111 -> 1 * (2*0) + 1 * (2*1) + 1 * (2*2) + 0 * (2*3) + 1 * (2*4)
#0 * (2*5) + 1 * (2*6) + 1 * (2*7) + 1 * (2*8)
#x | z if either is 1 then 1 else 0
print("the OR operator of x & z(276):", (x | z))
#XOR ^
#x -> 0b110010110
#z -> 0b101010101
#ans: 0b011000011 -> 1 * (2*0) + 1 * (2*1) + 0 * (2*2) + 0 * (2*3) + 0 * (2*4)
#0 * (2*5) + 1 * (2*6) + 1 * (2*7) + 0 * (2*8)
#x ^ z if one of them is 1, but not both, then 1 else 0
print("the XOR operator of x ^ z(276):", (x ^ z))
#masking
first_choice = True
second_choice = False
third_choice = True
#5
choices = 0b101
print(choices & 0b100) #mask - only le tthe first choice through if its there at all
print(choices & 0b010) #is second choice set? 2  if so else 0 
print(choices & 0b001) #is third choice set ? 1 if so else 0
#more bitwise examples
def greet():
    print("hey")
print("67 in base 2", bin(greet.__code__.co_flags))
#NOT (~) we think - tiide
print("z:",z)
#mutiply by 2 then * -1
print("NOT (~)")
print("~ z:",~z)
print("binary z:  ",bin(z))
print("swap the two digits from the right end of binary number")
print("binary ~z:",bin(~z))
print("z:",z)
#mutiply by 2
print("LEFT-SHIFT (<<)")
print("z << 1:",z <<1)
print("binary z:     ",bin(z))
print("adding 1 zero to the right end of binary number z")
print("binary z << 1:", bin(z <<1))
print("z:",z)
#mutiply by 4
print("z << 2:", z<<2)
print("binary z:     ",bin(z))
print("adding 2 zeros to the right end of binary number z")
print("binary z << 2:", bin(z <<2))
print("RIGHT-SHIFT (>>)")
# divide by 2
print("z:", z)
print("z >> 1:", (z >> 1))
print("binary z:    ", bin(z))
print("remove 1 number from right end of binary number z")
print("binary z >> 1", bin(z >> 1))
# divide by 4
print("z:", z)
print("z >> 2:", (z >> 4))
print("binary z:    ", bin(z))
print("remove 2 numbers from right end of binary number z")
print("binary z >> 2", bin(z >> 2))
