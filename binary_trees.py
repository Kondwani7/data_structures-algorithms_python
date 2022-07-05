#tree has a left andr right nodes
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data
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