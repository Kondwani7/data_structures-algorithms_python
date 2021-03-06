"""

#base2 - a sequence of 1s and 0s
#operateors:
#Bitwise AND (&)OR (|), XOR(^),NOT(!) XOR()
"""
#functions get a bit
from heapq import nsmallest
from os import GRND_RANDOM
from typing import List


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
print("the ith from the right end of binary number becomes 0")
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
# 
print("z:", z)
print("z >> 1:", (z >> 1))
print("binary z:    ", bin(z))
print("remove 1 number from right end of binary number z")
print("binary z >> 1", bin(z >> 1))
# 
print("z:", z)
print("z >> 2:", (z >> 4))
print("binary z:    ", bin(z))
print("remove 2 numbers from right end of binary number z")
print("binary z >> 2", bin(z >> 2))
#Questions
"""
Q1 - leetcode 136 single number
Given a non-empty array of integers nums, 
every element appears twice except for one. Find that single one.
e.g [2, 2, 1]
ans: 1
e.g 2 [4,1,2,1,2]
ans: 4
"""
def singleNumber(nums):
    """
    use XOR only 1-0 pair gives 1, else 0
    and multiply numbers on list by XOR
    in list if a number occurs twice its i ^ i which will be 0
    if a number occurs once its i ^ 0 which will be 1 : our answer
    """
    ans = 0
    for i in nums:
        ans = ans ^ i
    return ans
#test cases
list1 = [2, 2, 1]
list2 = [ -1, 0, 0 , -1 , 2, -2, 2]
list3 =  [4,1,2,1,2]
print("unique number in list1",singleNumber(list1))
print("unique number in list2",singleNumber(list2))
print("unique number in list3",singleNumber(list3))
"""
Q2
check if a number is even or odd
"""
def evenOdd(num):
    #use AND operator
    #if last part of binary is 1 then odd, else 0
    # AND - i & i
    if (num & 1) == 1:
        print(f"{num} :odd number")
    else:
        print(f"{num} even number")

evenOdd(5)
evenOdd(24)
evenOdd(1125)
"""
q3 find the ith bit in a number
e.g 13 get the 2th bit
13 in binary is 1101 - the 2th bit: 0
"""
def extractIthBit(num, i):
    """
    we use a mask spot the ith bith
    the ith bit can be spotted by left shift ith times 
    so mask= 1 << i
    then ith bit is number & mask
    start counting bits from 0... not 1..
    """
    mask = 1 << i
    num = num & mask
    if (num > 0):
        return 1
    else:
        return 0
print("2th bit in 13",extractIthBit(13, 0))
print("1th bit in 13",extractIthBit(13, 1))
print("2th bit in 13",extractIthBit(13, 2))
print("2th bit in 14",extractIthBit(13, 2))
"""
Q4
set our ith bit to 1
still using the mask and left shift <<
mask = 1 << i
then use OR |
"""
def setIthBit(num, i):
    """ 
    define our mask - 1<< i if i = 2 then 100 is mask
    or operation on mask and number
    if num is 13 and our ith bit =3 then 
    1101
    1000
    1101 = ans
    """
    mask = 1 << i 
    num = num | mask
    return num
print("set 1th bit to 0, new num:",setIthBit(13, 0))
print("set 1th bit to 1, new num:",setIthBit(13, 1))
print("set 1th bit to 2, new num:",setIthBit(13, 2))
print("set 1th bit to 3, new num:",setIthBit(13, 3))
"""
q5 set the ith bit in our number to zero
in essence ,clearing it
"""
def clearIthBit(num, i):
    """
    get mask = 1 << i
    NOT operation on mask = ~mask
    then AND operation on num & mask
    """
    mask = 1 << i
    mask = ~mask
    num = num & mask
    return num
print("clear 0th bit in 13, new num:", clearIthBit(13, 0))
print("clear 1th bit in 13, new num:", clearIthBit(13, 1))
print("clear 2th bit in 13, new num:", clearIthBit(13, 2))
print("clear 3th bit in 13, new num:", clearIthBit(13, 3))
#change ith bit to a new value
"""
q6
set our ith bit to a new defined value(1 or 0 because its binary)
"""
def changeIthBitt(num, i, value):
    """
    clear our old ith bit
    set(replace) our value(new) ith bit
    """
    #first clear - set to 0
    mask1 = i << i
    mask1 = ~mask1
    res = num & mask1
    #set our new valu to replace it
    mask2 = value << i
    res = res | mask2
    return res
print("change 1th bit to 1, new_num:", changeIthBitt(13, 1, 1))
print('change 2th bit to 1, new_num:', changeIthBitt(13, 2, 0))
"""
q1 hammering weight
Write a function that takes an unsigned integer and returns 
the number of '1' bits it has (also known as the Hamming weight).
"""
def hammeringWeight(n):
    """
    gets the number of "1" bits in a number converted to binary
    """
    #get our number and covert it to a binary string
    #initialize our count at 0
    #loop in binary string, for every 1 in the character, 
    #increase count by 1
    n = str(bin(n))
    #print to see binary
    print(n)
    count = 0
    for i in n:
        if i == "1":
            count += 1
    return count

print("number of 1s in 13:", hammeringWeight(13))
print("number of ones in z:", hammeringWeight(z))
print(bin(13))
print(bin(~13))
#find a missing number
"""
Leetcode
Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.
e.g [1, 3, 4, 6, 7]
missing number = 2
"""
#sum of numbers could be used to find it
#sum of numbers n *(n+1) /2
#then deducting sum from total lenght of numbers to get the missing number
print("missing number")
arr1 = [2, 4, 5, 6, 7]
def missingNumber(arr):
    ans = len(arr)
    for i in range(len(arr)):
        ans += (i - arr[i])
    return ans
print(missingNumber(arr1))