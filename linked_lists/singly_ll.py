class Node:
       def __init__(self, data=None):
        self.data = data
        self.next = None

class SLinkedList:
   def __init__(self):
      self.head = None

   def print_LL(self):
      n = self.head
      while n is not None:
            print(n.data)
            n = n.next

ll1 = SLinkedList()
ll1.head = Node(1)
n2 = Node(2)
n3 = Node(3)

#link nodes
ll1.head.next = n2
n2.next = n3

ll1.print_LL()

    
   


