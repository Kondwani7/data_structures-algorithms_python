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
    return num * mask
#
