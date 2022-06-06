#get the largest value in a vector
def get_largest(vec):
    #inital first value in the list
    n = vec[0]
    #loop through the entire vector
    for i in vec:
        if i > n:
            n = i
    return n
        

print(get_largest([1,2,3,6,15,3,15,6,7,9]))