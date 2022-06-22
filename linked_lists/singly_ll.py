from typing import List, Optional


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
        """
            Description:
                we will insert a new node in the a given postion of the linked list
            Args:
                newData - the data of our new node
                position - the position of our target node
            Returns:
                None
        """
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
        """
            Description:
                we will delete a new node in the first element of the linked list
            Returns:
                None
        """
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
        """
            Description:
                we will delete a new node in the last element of the linked list
            Returns:
                None
        """
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
        """
            Description:
                we will delete a new node in the first element of the linked list
            Args:
                position - the target position of the node that will be deleted
            Returns:
                None
        """
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
        """
            Description:
                this will reverse our linked list
                it will switch the roles of our initated current and previous nodes in a loop
                current --> previous --> null 
                Null <--previous <-- current (in a loop)
            Returns:
                None
        """
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
    def getMiddleNode(self):
        """
            Description:
                this function will get the middle node of our linked list
            Returns:
                the middle node of our linked list
            
        """
        fastPtr = self.head
        slowPtr = self.head
        if(self.head is None):
            return self.head
        else:
            while (fastPtr is not None and fastPtr.next is not None):
                #the slow pointer will move to its next in a loop
                slowPtr = slowPtr.next
                #the fast pointer will move twice as fast
                fastPtr = fastPtr.next.next
            #finally we will get the slowPtr, now the mid point
            return print(f"middle node of linked list: {slowPtr.data}")

    #find the nth node from the end of the linked list
    def getNthNodeEnd(self, n):
        """
        Description:
            this function gets the nth (a given postion) node from the end of the linked list
        Args:
            n - the target nth node's position
        Returns:
            the nth node's data and next
        """
        #target node
        mainPtr = self.head
        #reference for the last node on the list
        refPtr = self.head
        count = 0
        if (n< 0):
            return print("invalid value")
        elif (self.head is None):
            return print(f"linked list is null: {self.head}")
        else:
            while (count < n):
                if (refPtr is None):
                    print("n is greater the number of nodes in the linked list")
                #move the ref pointer to the nth node
                refPtr = refPtr.next
                count+=1
            #move the main pointer to the target nth node
            while (refPtr is not None):
                #the ref pointer is now at the nth of the list
                refPtr = refPtr.next
                #now the main pointer will move to the nth node
                mainPtr = mainPtr.next
            return print(f"the nth node's data:{mainPtr.data} and it's next: {mainPtr.next}")
    #remove duplicates in a sorted link list
    def removeDuplicateNodes(self):
        """
        Description:
            this function removes nodes with duplicate data in a sorted link list
        Returns:
            None
        """
        current = self.head
        while (current is not None and current.next is not None):
            #if there is a duplicate
            if(current.data == current.next.data):
                #loop to the next node, in turn deleting the duplicate
                current.next = current.next.next
            else:
                #loop to the end
                current = current.next
    # insert a node in a sorted link list
    def insertSorted_LL(self,newData):
        """
        Description:
            this function inserts data in the sorted linked list
        
        Returns:
            head of the link list
        """
        current = self.head
        newNode = Node(newData)
        
        temp = None
        if (current is None):
            return newNode.data
        else:
            while(current is not None and current.data < newNode.data):
                temp = current
            # temp --> current in a loop till the new node reached
                current = current.next
            # the new node's pointer becomes the current
            # newNode --> current
            newNode.next = current
            #the temp now points the the newNode, completing the insertion
            #temp --> newNode --> current
            temp.next = newNode
        return print(self.head.data)
#detect a loop in a linked list
    def detectLoop_LL(self):
        """
        Description:
            This function detects if a linked list has a loop
        Returns:
            - a boolean (True) if the linked list is has a loop
            - a boolean (False) if the linked list does not have a loop
        """
        fastPtr = self.head
        slowPtr = self.head

        if (self.head is None and self.head.next is None):
            return print("empty linked list")
        else:
            while (fastPtr != None and fastPtr.next != None):
                fastPtr = fastPtr.next.next
                slowPtr = slowPtr
                #if the meet in the loop
                if(slowPtr == fastPtr):
                    return print(f"linked list is a loop: {True}")
            return print(f"linked list is not a loop: {False}")
    
    
    #detecting starting node of a linked list in a loop
    def detectStartNodeLoop(self):
        """
        Description:
            This function detects if a linked list has a loop
        Args:
            - getStartingNode(slowPtr) - this function finds the position of the slowPtr and and replaces its with a temp node
                                       - it then returns the temp's data 
        Returns:
            - a boolean (True) if the linked list is has a loop
            - a boolean (False) if the linked list does not have a loop
        """
        fastPtr = self.head
        slowPtr = self.head
        if (self.head is None and self.head.next is None):
            return print("empty linked list")
        else:
            while (fastPtr != None and fastPtr.next != None):
                fastPtr = fastPtr.next.next
                slowPtr = slowPtr
                #if the meet in the loop
                if(slowPtr == fastPtr):
                    return self.getStartingNode(slowPtr)
            return print(f"linked list is not a loop: {False}")

    def detectLoop(self, loop_node):
            temp = self.head
            while(slowPtr != temp):
                temp = temp.next
                slowPtr = slowPtr.next
            return print(f"starting node in loop: {temp.data}")

    #delete a loop in a linked llst
    def deleteLoop_LL(self):
        fastPtr = self.head
        slowPtr = self.head
        if(self.head == None and self.head.next == None):
            return print("linked list is empty")
        else:
            if(fastPtr != None and fastPtr.next != None):
                fastPtr = fastPtr.next.next
                slowPtr = slowPtr.next
            #if there is a loop
            if(slowPtr == fastPtr):
                return self.removeLoop(loop_node=slowPtr)

    #delete a loop
    def removeLoop(self, loop_node):
        ptr1 = loop_node
        ptr2 = loop_node
        #count number of nodes in the loop
        n = 1
        while(ptr1.next != ptr2):
            ptr1 = ptr1.next
            n+=1
        #fix ptr1 to head
        ptr1 = self.head
        for i in range(n):
            ptr2 = ptr2.next
        #move both pointers to the same position
        while(ptr2 != ptr1):
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        #last node
        while (ptr2.next != ptr1):
            ptr2 =ptr2.next
        #delete the loop
        ptr2.next = None
         
    #merge two sorted linked lists
    def mergetwo_SortedLL(self, a:Node, b:Node) -> Node:
        """
        Description:
            This function gets to sorted lists and merges them into one sorted list
        Args:
            a - the first list
            b - the second list
        Returns:
            the new merged list
        """
        #define a dummy with next null
        dummy = Node()
        tail = dummy
        while(a and b):
            if(a.data <= b.data):
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
        tail = tail.next
        #if the loop broke while one of the lists is empty but not all nodes in 2 lists have been merged
        if (a):
            tail.next = a
        else:
            tail.next = b
        #new sorted list
        #go to the next to avoid the 0 node 
        return dummy.next
    #merge k sorted lists
    def mergeK_SortedLL(self, lists: List[Node]) -> Node:
        """
        Description:
            This function merges k number of sorted lists
        Returns:
            The new merged list
        """
        #if the lists are empty
        if not lists or len(lists) == 0:
            return None
        #while we have more than one list
        while len(lists) > 1:
            mergedLists =  []
            #the merging is happpening with 2 lists, hence looping by 2
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                #if the len of lists is odd merge list 1 with a None type, which is just l1
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists(self.mergetwo_SortedLL(l1, l2))
            lists = mergedLists
            #return the merged list
            return lists[0]
    #remove the nth node from a linked list
    def removeFromNthNode(self, head: Optional[Node], n: int) -> Optional[Node]:
        #dummy node points at head
        dummy = Node(0, head)
        #the left will start at dummy, until it gets to one node before our target
        left = dummy
        right = head
        while n > 0 and right:
            right = right.next
            n-=1
        while right:
            right = right.next
            left = left.next
        #delete the node
        left = left.next.next
        return dummy.next
    
    def removeMiddleNode(self, head: Optional[Node]) -> Optional[Node]:
        #node before the head
        dummy = Node(0, head)
        slowPtr = dummy
        fastPtr = head
        while fastPtr and fastPtr.next:
            #fast pointer moves 2 times
            fastPtr = fastPtr.next.next
            #slow pointer moves 1 until it gets to the node before the middle Node
            slowPtr = slowPtr.next
        #delete the middle node
        slowPtr.next = slowPtr.next.next
        #return the updated list
        return dummy.next
    





    



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
#ll1.print_LL()
#reverse list
#ll1.reverse_LL()
#print reversed list
#ll1.print_LL()
#ll1.getMiddleNode()
#ll1.getNthNodeEnd(2)
#ll1.insertPosition(2,6)
#ll1.insertPosition(5,12)
#ll1.print_LL()
#remove duplicates
#ll1.removeDuplicateNodes()
#ll1.print_LL()
#ll1.insertSorted_LL(7)
#ll1.print_LL()
#a linked list with a loop

ll2 = SLinkedList()
#head
ll2.head = Node(1)
node2 = Node(2)
node3 = Node(4)
node4 = Node(6)
node5 = Node(8)
node6 = Node(10)
node7 = Node(12)
#assign pointers
ll2.head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
#loop begins at 3
node7.next = None
#ll2.print_LL()

"""
redo delete a loop and detect a loop
"""
#ll1.print_LL()
#ll2.print_LL()
#merge
result = SLinkedList()
result.head = result.mergetwo_SortedLL(ll1.head, ll2.head)
result.print_LL()




