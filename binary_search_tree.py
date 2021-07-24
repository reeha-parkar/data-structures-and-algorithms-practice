
class Node:
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None

#inorder traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=' ')
        inorder(root.right)


#insert a new node
#first, the root is checked, then recursively, we reach till there is empty space
def insert(node, key):
    if node is None:
        return Node(key) # empty space is there, so insert the new node
    else:
        #check if 
        if node.value == key:
            return node
        elif node.value < key:
            node.right = insert(node.right, key)
        else:
            node.left = insert(node.left, key)
    return node

#search the key
def search(root, key):

    if root is None or root.value == key:
        return root
    if key > root.value:
        return search(root.right, key)
    return search(root.left, key)
    


bst = Node(50) #created root node
bst = insert(bst, 20)
bst = insert(bst, 40)
bst = insert(bst, 30)
bst = insert(bst, 70)
bst = insert(bst, 80)
bst = insert(bst, 60)
bst = insert(bst, 90)

# print the tree
inorder(bst)

print("\nFinding if 30 is present")
if search(bst, 100):
    print("FOUND")
else:
    print("NOT FOUND")



