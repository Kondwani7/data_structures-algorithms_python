#dynamic programming 
#bottom up (build up from a sub problem & solution and sub up solutions) and top down approach
#recursion + memorization
# a chuck load of practice makes prefect
#example 1 fibonacci number
def fib(n):
    """
    leetcode
    The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
     such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
    F(0) = 0, F(1) = 1
    F(n) = F(n - 1) + F(n - 2), for n > 1.
    """
    #top down
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        #left and right pointer is the sum of the last 2 numbers recursively updated
        l = fib(n-1)
        r = fib(n-2)
        return l + r

fib(5)
#fib with the bottom up appraoch, store in a table
def fib2(n):
    table = [0] * 50
    table[0] = 0
    table[1] = 1
    for i in range(2, n+1):
        table[i] = table[i-1] + table[i-2]
    return table[n]