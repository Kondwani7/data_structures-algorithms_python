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

