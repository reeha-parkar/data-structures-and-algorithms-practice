class Node:
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=' ')
        inorder(root.right)

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.value == key:
            return root
        elif key > root.value:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

bst = Node(1)
bst = insert(bst, 7)
bst = insert(bst, 4)
bst = insert(bst, 3)
bst = insert(bst, 6)
bst = insert(bst, 2)
bst = insert(bst, 9)
bst = insert(bst, 8)
bst = insert(bst, 5)
inorder(bst)

