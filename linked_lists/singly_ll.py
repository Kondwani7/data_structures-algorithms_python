from turtle import pos
from requests import head


class Node:
       def __init__(self, data=None):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        """
        Description:
            set our linked list's head
        """
        self.head = None
    #print the linked list   
    def print_LL(self):
        """
        Description:
            print our linked list
        Returns:
            a linked list    
        """
        current = self.head
        while current is not None:
                print(f"{current.data}-->")
                current = current.next
        #end of list: null pointer
        print("null")
    #get the length of the linked list\
    def length_ll(self):
        """
        Description:
            print the length of a linked list
        Returns:
            lenghth of linked list
        """
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
        """
            Description:
                we will insert a new node in the first element of the linked list
            Args:
                newData - the data of our new node
            Returns:
                None
        """
        newNode = Node(newData);
        #make the new node's next point at the head
        newNode.next = self.head
        #new node is the head
        self.head = newNode
    #insert at the end of the linked list
    def insertEnd(self, newData):
        """
            Description:
                we will insert a new node in the last element of the linked list
            Args:
                newData - the data of our new node
            Returns:
                None
        """
        newNode  = Node(newData)
        #current node that points at the head
        current = self.head
        if current is None:
            current.next = newNode
        else:
            #travsere to the end
            while current.next is not None:
                #get the end of the list
                current = current.next
            #the current's next pointer will now point to the newNode
            current.next = newNode
    #insert at a target position
    def insertPosition(self,position, newData):
        newNode = Node(newData)
        
        #if the list is empty
        if(position ==1):
            newNode.next = self.head
            #the new Node is now the head
            self.head = newNode
        else:
            #the node before our target
            previous = self.head
            count = 1
            #traverse the the node just before our target position
            while (count < position -1):
                # prev-next> target-pos ->..
                previous = previous.next
                count+=1
            #our  current node now points at the previous' next pointer
            #current --> target-position
            current = previous.next
            #the previous next becomes the newNode
            #previous- next-> == newNode
            previous.next = newNode
            #the newNode's next pointer becomes the current
            #newNode-next--> current
            newNode.next = current
    #delete the first element in the list
    def deleteFirst(self):
        #if the list is empty
        if (self.head is None):
            self.head = None
        else:
            #temp node set is the head
            temp = self.head
            #make the head point at it's next, in removing it
            self.head = self.head.next
            #set the temp's next to point to null to delete the head
            temp.next = None
    def deleteLast(self):
        #if the list is empty
        if(self.head == None and self.head.next == None):
            self.head = None
        else:
            current = self.head
            previous = None
            #traverse to the end of the linked list
            while(current.next is not None):
                #update the previous as current
                previous = current
                #get to the end
                current = current.next
            #make the previous's next pointer point to null, deleting it in the process
            previous.next = None
    #remove at a target postion
    def deletePostion(self, position):
        #if the list is null
        if (position == 1):
            self.head = self.head.next
        else:
            previous = self.head
            count = 1
            while (count < position -1):
                #break loop
                previous = previous.next
                count +=1
            #the previous'next is current, not targetNode
            current = previous.next
            #delete our target node from the list
            previous.next = current.next
    #check if a specific value is in one of the nodes in the linked list
    def searchValue( targetData):
        pass
    #reverse a linked list
    def reverse_LL(self):
        current = self.head
        previous = None
        #traverse through each node in the list
        while (current is not None):
            next = current.next
            current.next = previous
            #previous takes current's position
            previous = current
            #current takes the next position
            current = next
        #now the previous is head of the list after the end of the loop
        self.head = previous
    #find the middle node in the linked list
    #find the nth node from the end of the linked list
    #remove duplicates




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
ll1.insertEnd(15)
ll1.insertPosition(5,12)
ll1.deleteFirst()
ll1.insertEnd(18)
ll1.deleteLast()
ll1.insertPosition(4, 10)
#ll1.print_LL()
ll1.deletePostion(4)
#print list
ll1.print_LL()
#reverse list
ll1.reverse_LL()
#print reversed list
ll1.print_LL()
    
   


