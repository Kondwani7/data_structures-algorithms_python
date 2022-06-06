#What is the tightest upper-bound for the time complexity 
def distance(a):
    n = len(a)
    #before the last element
    for i in range(n -1):
        #second element and the last element in the list
        for j in range(i + 1, n):
            # the second element minus the element behind it in the list
            # [a, b,c] => b-a, c-a, c-b
            print("%d - %d = %d" %(a[j], a[i], a[j]-a[i]))

distance([3,2,4, 5])
#big O notation  = O(n^2)