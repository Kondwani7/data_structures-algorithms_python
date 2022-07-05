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
    #inorder traversal
    # left -> root -> right
    def inOrderTraversal(self, root):
        res = []
        if root:
            res = self.inOrderTraversal(root.left)
            res.append(root.data)
            res = res + self.inOrderTraversal(root.right)
        return res
    #preorder traversal
    #root -> left -> right
    def preOrderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preOrderTraversal(root.left)
            res = res + self.preOrderTraversal(root.right)
        return res
    #post order traversal
    #left -> right -> root
    def postOrderTraversal(self, root):
        res = []
        if root:
            res = self.postOrderTraversal(root.left)
            res = res + self.postOrderTraversal(root.right)
            res.append(root.data)
        return res
bt1 = Node(21)
bt1.insert(19)
bt1.insert(18)
bt1.insert(22)
bt1.insert(23)
bt1.insert(24)
bt1.insert(16)
#bt1.PrintTree()
print("preorder traversal: ",bt1.inOrderTraversal(bt1))
#in order traversal
print("preorder traversal: ", bt1.preOrderTraversal(bt1))
#post order traversal
print("post order traversal: ", bt1.postOrderTraversal(bt1))