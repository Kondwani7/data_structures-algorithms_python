#time complexity O(1)
#key-value store
#e.g find a repeated character
def firstReapeatdChar(s):
    size = len(s)
    count = [0] * 256
    for i in range(size):
        if (count[ord(s[i])] == 1):
            print(s[i])
            break
        else:
            count[ord[s[i]]] += 1
    #when no repeated
    if(i==size):
        print("not repeated charcaters")
    return 0

s1 = ["a", "b", "c", "b", "d"]
print(firstReapeatdChar(s1))