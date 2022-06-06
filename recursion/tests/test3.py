#What is the tightest upper-bound for the time complexity 
def  tricky(n):
    operations =  0
    while n > 0:
        for i in range(n):
            #get the number of operations performed
            print(f"Operations:{operations}")
            operations += 1
        n = int(n/2)

tricky(5)
#the big O notation - O(n^2)