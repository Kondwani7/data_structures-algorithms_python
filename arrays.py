import array as arr

a = arr.array('i',[1,2,3])
for i in range(0, 3):
    print(a[i], end=' ')
print()
b = arr.array('d', [3.4, 2.4, 5.44, 0.56])
for i in range(0, 4):
    print(b[i], end=" ")
print()

#get a specific element in a array
print(f"third element in array: {a[2]}")
#append at the end
a.append(4)
#append at a specific position
# first position  (0)
a.insert(0,0)
#third position (2)
a.insert(2,2)
for i in range(0, 6):
    print(a[i], end=' ')
print()
#remove an element at a specific position (4)
a.pop(4)
for i in range(0,5):
    print(a[i], end=' ')
print()