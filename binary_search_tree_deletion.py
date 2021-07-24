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

def min_value_node(node):
    current = node
    while current.left != None:
        current = current.left
    return current

def delete(root, key):
    if root is None:
        return root

    if key < root.value:
        root.left = delete(root.left, key)

    elif key > root.value:
        root.right = delete(root.right, key)

    #reached the node to be deleted
    else:

        #if node to be deleted has one or zero child
        if root.left is None:
            temp = root.right
            root = None
            return temp
        
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        #for node having 2 children
        temp = min_value_node(root.right)
        root.value = temp.value
        root.right = delete(root.right, temp.value)
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
print()
delete(bst, 4)
inorder(bst)

