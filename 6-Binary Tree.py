
__author__ = 'Metehan Özcan'
"""_summary_
    Binary Search Tree Impletementation
    Binary Search Tree Complexities
    Time Complexity
    Operation	Best Complx	Average-- 	Worst Case Complexity
    Search	    O(log n)	O(log n)	O(n)
    Insertion	O(log n)	O(log n)	O(n)
    Deletion	O(log n)	O(log n)	O(n)
    
    Space Complexity
    The space complexity for all the operations is O(n).
    Returns:
        _type_: _description_
    """


class Queue:  # * For level order traversal. 
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        if item is None:
            return 'Not valid'
        self.queue.append(item)

    def pop(self):
        if self.empty():
            return 'Empty'
        return self.queue.pop(0)

    def empty(self):
        return len(self.queue) == 0


class Node(): #* For nodes.
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def findMin(self):
        if(self.left):
            return self.left.findMind()
        else:
            # print(self.data)
            return self.data

    def insert(self, data):
        # print(self.data,data)
        if(self.data is data):
            return 'Duplicate not allowed.'

        elif(self.data > data):
            if(self.left):
                self.left.insert(data)
            else:
                self.left = Node(data)
        else:
            if(self.right):
                self.right.insert(data)
            else:
                self.right = Node(data)

    def delete(self, data):
        if (data < self.data and self.left):
            self.left = self.left.delete(data)
        elif(data > self.data and self.right):
            self.right = self.right.delete(data)
        else:
            if(self.data == data):
                if(self.right and self.left):
                    minVal = self.right.findMin()
                    self.data = minVal
                    self.right = self.right.delete(minVal)
                elif(self.left):
                    return self.left
                elif(self.right):
                    return self.right
                else:
                    return None
        return self

    def search(self, data):
        if(self.data == data):
            return self.data, True
        elif (data < self.data and self.left != None):
            return self.left.search(data)
        elif (data > self.data and self.right != None):
            return self.right.search(data)
        return False


class BST(): #* Tree constructor.
    def __init__(self):
        self.root = None

    def height(self, root):
        if root is None:
            return -1
        l = self.height(root.left)
        r = self.height(root.right)
        return max(l, r)+1

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(str(root.data)+'->', end='')
        self.inorder(root.right)
        
    def postorder(self, root):
        if root is None:
            return
        self.inorder(root.left)        
        self.inorder(root.right)
        print(str(root.data)+'->', end='')
        
    def preorder(self, root):
        if root is None:
            return
        print(str(root.data)+'->', end='')
        self.inorder(root.left)        
        self.inorder(root.right)

    def insert(self, data):
        if self.root:
            self.root.insert(data)
        else:
            self.root = Node(data)

        return self.root

    def delete(self, data):
        if self.root:
            self.root = self.root.delete(data)

    def search(self, data):
        return self.root.search(data)  

        

    def levelorder(self, root):

        q = Queue()
        q.enqueue(root)

        while (not q.empty()):

            root = q.pop()
            print(root.data, end="->")

            if root is not None:
                q.enqueue(root.left)
                q.enqueue(root.right)
        return 'End'

    def isFullTree(self, root):

        # Tree empty case
        if root is None:
            return True

        # Checking whether child is present
        if root.left is None and root.right is None:
            return True

        if root.left is not None and root.right is not None:
            return (self.isFullTree(root.left) and self.isFullTree(root.right))

        return False


tree = BST()
tree.insert(5)
tree.insert(6)
tree.insert(7)
tree.insert(4)
tree.insert(3)
tree.insert(2)
tree.insert(8)

print(tree.levelorder(tree.root))
print(tree.inorder(tree.root))
tree.delete(8)
print(tree.height(tree.root))
print(tree.inorder(tree.root))
print(tree.preorder(tree.root))
print(tree.postorder(tree.root))
print(tree.search(8))
print(tree.isFullTree(tree.root))
