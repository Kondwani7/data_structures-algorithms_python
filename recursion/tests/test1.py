#What is the tightest upper-bound for the time complexity 
def print_info(a):
    n = len(a)
    avg = 0.0
    for i in range(n):
        print(f"Element {i} is {a[i]}")
        #summing up all the elements in our list
        avg += a[i]
    #then dividing it by the length of the array
    avg /= n
    print(f"average is {avg}")


print_info([1,2,2,4])

#the big O notation = O(n)