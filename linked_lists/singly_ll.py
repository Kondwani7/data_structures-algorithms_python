class Node:
       def __init__(self, data=None):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
    #print the linked list   
    def print_LL(self):
        current = self.head
        while current is not None:
                print(f"{current.data}-->")
                current = current.next
        #end of list: null pointer
        print("null")
    #get the length of the linked list\
    def length_ll(self):
        count = 0
        current = self.head
        if current is None:
            print
        #traverse through the linked list
        while current is not None:
            count+=1
            #end at the null value, of the list
            current = current.next
        print(f"list length: {count}")
    # insert node at begining of linked list
    def insertFirst(self, newData):
        newNode = Node(newData);
        #make the new node's next point at the head
        newNode.next = self.head
        #new node is the head
        self.head = newNode

ll1 = SLinkedList()
ll1.head = Node(3)
n2 = Node(6)
n3 = Node(9)

#link nodes
ll1.head.next = n2
n2.next = n3

#get list length
#ll1.length_ll()
#insert at beginning of linked list
ll1.insertFirst(1)
print(ll1.head.data)
#print list
ll1.print_LL()
    
   


