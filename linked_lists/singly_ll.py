#singly linked list
class Node:
    #constructor
    def __init__(self, data):
        self.data = data
        self.next = None
   
        
class LinkedList(object):
    def __init__(self):
        self.head = None;


node1 = Node(10)
 
print(node1)