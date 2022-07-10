#backtracking is just another form of recursion
def permute(list, s):
    if list == 1:
        return s
    else:
        return [
                 y + x
                 #recursion in the first and last element
                 for y in permute(1, s)
                 for x in permute(list -1,s)
               ]

print(permute(3, ["(", ")"]))
print(permute(4, ["(",")"]))
