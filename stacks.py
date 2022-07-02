#LIFO
from collections import deque
from inspect import stack


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
#a stack with a linked list
class Node:
    def __init__(self, data):
        self.data = data,
        self.next = None
class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0
    #string representation of a stack
    def __str__(self):
        cur = self.head.next
        out = " "
        while cur:
            out += str(cur.data) + "->"
            cur = cur.next
        return out[:-3]
    #get current size of stack
    def getSize(self):
        return self.size
    #check if stack is empty
    def isEmpty(self):
        return self.size == 0
    #get top item of stack
    def peek(self):
        if self.isEmpty():
            raise Exception("peeking from an empty stack")
        #else
        return self.head.next.data
    #push value into the stack
    def push(self, data):
        node = Node(data)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
    #remove value from stack
    def pop(self):
        if self.isEmpty():
            raise Exception("popping an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size += -1
        return remove.data

stack3 = Stack()
for i in range(1, 11):
    stack3.push(i)
print(f"Stack3: {stack3}")
#popping
for i in range(1,6):
    remove = stack3.pop()
    print(f"popping: {remove}")
print(f"stack3 popped: {stack3}")

#reverse a string
def reverse(s):
    str1 = ""

    for i in s:
        str1 = i+ str1
    return str1
    

print(reverse("geeks"))
#reverse a string with recursion
def reverse_rec(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:] + s[0])
print(reverse_rec("quacks"))

def createStack():
    stack = []
    return stack
def size(stack):
    return len(stack)
def isEmpty(stack):
    if size(stack) == 0:
        return True
def push(stack, item):
    stack.append(item)
def pop(stack):
    if isEmpty(stack): return
    return stack.pop()
def reverse_stack(string):
    n = len(string)
    stack = createStack()
    for i in range(0, n, 1):
        push(stack, string[i])
    string = ""
    for i in range(0, n ,1 ):
        string += pop(stack)
    return string

print(reverse_stack("ddede"))