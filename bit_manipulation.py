"""

#base2 - a sequence of 1s and 0s
#operateors:
#Bitwise AND (&)OR (|), XOR(^),NOT(!) XOR()
"""
#functions get a bit
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
#ans: 0b100010100 -> 0 *(2^0) + 0 *(2^1) + 1 *(2^2) + 0 *(2^3) + 1 *(2^4)
# 0 *(2^5) + 0 *(2^6) + 0 *(2^7) + 1 *(2^8)  
print("the AND operator of x & z(276):", (x & z))

