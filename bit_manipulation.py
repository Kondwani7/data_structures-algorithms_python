"""

#base2 - a sequence of 1s and 0s
#operateors:
#Bitwise AND (&)OR (|), XOR(^),NOT(!) XOR()
"""
#functions get a bit
def getBit(num , i):
    return ((num & (1 << i)) != 0)
