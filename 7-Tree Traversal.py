"""
    Tree Traversal Implementation
    Functional Type--


    """
__author__ = 'Metehan Özcan'


class Node:
    def __init__(self, data=None, right=None, left=None):
        self.data = data
        self.right = right
        self.left = left


def insert(root, data):
    # Return a new node if the tree is empty
    if root is None:
        return Node(data)
    # Traverse to the right place and insert the node
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root


def findmin(root):
    current = root
    while current.left:
        current = current.left
    return current


def delete(root, data):
    if not root:
        return None
    elif data < root.data: #* If 
        root.left = delete(root.left, data)
    elif data > root.data:
        root.right = delete(root.right, data)
    else:  # * Found
        if not root.right and not root.left:  # * No child case. Root is None
            root = None
        elif not root.left:  # * One child case
            root = root.right

        elif not root.right:  # * One child case
            root = root.left

        else:  # * Both child case
            minval = findmin(root.right)
            root.data = minval.data
            root.right = delete(root.right, minval.data)
    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end='->')
        inorder(root.right)
    return 'END'


def inorder_iter(root):
    s = []
    curr = root
    while s or curr:
        if curr:
            s.append(curr)
            curr = curr.left
        else:
            curr = s.pop()
            print(curr.data, end='->')

            curr = curr.right
    return 'END'


def preorder(root):
    if root:
        print(root.data, end='->')
        preorder(root.left)
        preorder(root.right)
    return 'END'


def preorder_iter(root):
    s = []
    s.append(root)
    while s:
        node = s.pop()
        print(node.data, end='->')
        if node.right:
            s.append(node.right)
        if node.left:
            s.append(node.left)
    return 'END'


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end='->')
    return 'End'


def postorder_iter(root):
    if root is None:
        return
    s1 = []
    s2 = []
    s1.append(root)
    while s1:
        node = s1.pop()
        s2.append(node)

        if node.left:
            s1.append(node.left)
        if node.right:
            s1.append(node.right)

    while s2:
        node = s2.pop()
        print(node.data, end='->')
    return 'End'


def levelorder_traversal(root):
    q = [root]

    while len(q) > 0:
        root = q.pop(0)
        if root is not None:
            print(root.data, end='->')
            q.append(root.left)
            q.append(root.right)

    return 'End'


def reverse_levelorder_traversal(root):
    q = [root]
    s = []

    while len(q) > 0:
        root = q.pop(0)
        if root is not None:
            s.append(root)
            q.append(root.right)
            q.append(root.left)

    while s:
        node = s.pop()
        print(node.data, end='->')

    return 'End'


root = None
root = insert(root, 5)
root = insert(root, 2)
root = insert(root, 3)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = delete(root, 8)
# root = Node(2)
# root.left = Node(1)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.left = Node(6)
# root.right.right = Node(7)
# root.left.left.left = Node(8)
print('inorder traversal')
inorder(root)
print('\ninorder iter traversal')
print(inorder_iter(root))
print('preorder traversal')
print(preorder(root))
print('preorder iter traversal')
print(preorder_iter(root))
print('postorder traversal')
print(postorder(root))
print('postorder iter traversal')
print(postorder_iter(root))
print('levelorder traversal')
print(levelorder_traversal(root))
print('reverse level order traversal')
print(reverse_levelorder_traversal(root))
