#tree has a left andr right nodes
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    #insertion
    def insert(self, data):
        #binary tree, if less than curr node go to the left side
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        #if greater than curr node go the right side
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                #recursively update
                self.right.insert(data)
        #if the binary tree is empty
        else:
            self.data = data
    #print data
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()


bt1 = Node(21)
bt1.insert(19)
bt1.insert(18)
bt1.insert(22)
bt1.insert(23)
bt1.insert(24)
bt1.insert(16)
bt1.PrintTree()