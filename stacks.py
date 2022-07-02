#LIFO
from collections import deque


stack1 = []
stack1.append(1)
stack1.append(3)
stack1.append(5)
print(f"initial stack:{stack1}")
stack1.pop()
print(f"popped stack:{stack1}")
#implement a stack with deqeue
stack2 = deque()
stack2.append(2)
stack2.append(4)
stack2.append(6)
stack2.append(10)
print(f"stack 2:{stack2}")
stack2.pop()
print(f"stack 2 popped: {stack2}")