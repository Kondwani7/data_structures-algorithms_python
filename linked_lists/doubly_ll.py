from typing import Optional


class Node:
    def __init__(self, data=None, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous

class DLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    #print a doubly linked list
    def print_DLL(self, head: Optional[Node]) -> Optional[Node]:
        temp = head
        #while the temp value is not empty
        while temp:
            print(f"{temp.data}-->")
            temp = temp.next
    #add node at front of list
    def push_first(self, newData):
        newNode = Node(newData)
        newNode.next = self.head
        newNode.previous = None
        if self.head:
            self.head.prev = newNode
            self.head = newNode
            newNode.prev = None
        #if empty make the new node the head and tail
        else:
            self.tail.next = newNode
            newNode.next = None
            self.tail = newNode

    