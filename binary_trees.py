#tree has a left andr right nodes
from collections import deque


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
        if root is None:
            return res
        if root:
            res = self.inOrderTraversal(root.left)
            res.append(root.data)
            res = res + self.inOrderTraversal(root.right)
        return res
    #preorder traversal
    #root -> left -> right
    def preOrderTraversal(self, root):
        res = []
        if root is None:
            return res
        if root:
            res.append(root.data)
            res = res + self.preOrderTraversal(root.left)
            res = res + self.preOrderTraversal(root.right)
        return res
    #post order traversal
    #left -> right -> root
    def postOrderTraversal(self, root):
        res = []
        if root is None:
            return res
        if root:
            res = self.postOrderTraversal(root.left)
            res = res + self.postOrderTraversal(root.right)
            res.append(root.data)
        return res
    #level order traversal
    # root -> level 1 (left and right) ... level n (left and right)
    #use a queue because of FIFO
    def levelOrderTraversal(root):
        res = []
        if root is None:
            return res

        q = deque()
        q.append(root)
        while q:
            currSize = len(q)
            currList = []
            while currSize > 0:
                currNode = q.popleft()
                currList.append(currNode.data)
                currSize -= 1
                #check if it has  a left child
                if currNode.left:
                    q.append(currNode.left)
                #check for right childd
                if currNode.right:
                    q.append(currNode.right)
            res.append(currList)
        return res

#find maximum in binary tree
def findMax(root):
    if root is None:
        return
    res = root.data
    lres = findMax(root.left)
    rres = findMax(root.right)
    if lres > rres:
        res = lres
    if rres > lres:
        res = rres
    return res
def findMin(root):
    if root is None:
        return
    res = []
    res = root.data
    lres = findMin(root.left)
    rres = findMin(root.right)
    if lres < rres:
        res = lres
    if rres < lres:
        res = rres
    return res

if __name__ == '__main__':
    bt1 = Node(21)
    bt1.insert(19)
    bt1.insert(18)
    bt1.insert(22)
    bt1.insert(23)
    bt1.insert(24)
    bt1.insert(16)
    bt1.insert(32)
    bt1.insert(14)
    bt1.insert(34)
    bt1.insert(13)
    bt1.insert(38)
    bt1.insert(11)
    #bt1.PrintTree()
    print("preorder traversal: ",bt1.inOrderTraversal(bt1))
    #in order traversal
    print("preorder traversal: ", bt1.preOrderTraversal(bt1))
    #post order traversal
    print("post order traversal: ", bt1.postOrderTraversal(bt1))
    #level order traversal
    print("level order traversal: ", bt1.levelOrderTraversal())


class binarySearchTree:
    def __init__(self, data):
        self.left =  None
        self.right = None
        self.data = data
    # insert the data
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = binarySearchTree(data)
                else:
                    self.left.insert(data)
            if data > self.data:
                if self.right is None:
                    self.right = binarySearchTree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    #compare value with nodes
    def findVal(self, compareVal):
        if compareVal < self.data:
            if self.left is None:
                return str(compareVal) + "not found"
            return self.left.findVal(compareVal)
        elif compareVal > self.data:
            if self.right is None:
                return str(compareVal) + "Not found"
            return self.right.findVal(compareVal)
        else:
            print(str(self.data) + " found")

bst1 = binarySearchTree(7)
bst1.insert(1)
bst1.insert(3)
bst1.insert(5)
bst1.insert(9)
bst1.insert(11)
bst1.insert(13)
print(bst1.findVal(7))