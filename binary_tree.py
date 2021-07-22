class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def inorder(node):
    if node==None:
        return

    inorder(node.left)
    print(node.key, end=' ')
    inorder(node.right)


def insert(node, key):
    if node==None:
        root = Node(key) # create a new node, we reached end of tree
        return

    temp = []
    temp.append(node)

    # level order traversal until we find an empty place
    while(len(temp)):
        node = temp[0]
        temp.pop(0)

        if node.left==None:
            node.left = Node(key)
            break
        else:
            temp.append(node.left)

        if node.right==None:
            node.right = Node(key)
            break
        else:
            temp.append(node.right)

def delete_deepest(root, d_node):
    temp = []
    temp.append(root)
    while(len(temp)):
        node = temp.pop(0)
        
        if node is d_node:
            node = None
            return
        
        if node.right:
            if node.right is d_node:
                node.right = None
                return
            else:
                temp.append(node.right)

        if node.left:
            if node.left is d_node:
                node.left = None
                return
            else:
                temp.append(node.left)
                
                
def delete(root, key):

    if root==None:
        return None
    
    if root.left==None and root.right==None:
        return None if root.key==key else root

    key_node = None
    temp = []
    temp.append(root)

    while(len(temp)):
        node = temp.pop(0)
        if node.key==key:
            key_node = node
            
        if node.left:
            temp.append(node.left)

        if node.right:
            temp.append(node.right)
            
    #got the key_node
    if key_node:
        value = node.key
        delete_deepest(root, node)
        key_node.key = value

    return root
    


if __name__=='__main__':

    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right = Node(3)

    #Inorder traversal
    print("Inorder traversal before insertion:", end=' ')
    inorder(root)

    print()
    insert(root, 12)
    inorder(root)
    print()
    insert(root, 13)
    inorder(root)
    print()
    insert(root, 7)
    inorder(root)
    print()
    insert(root, 8)
    inorder(root)

    print()

    print("Inorder traversal after insertion:", end=' ')
    inorder(root)

    print()

    print("Deleting a node (say, 8)")
    delete(root, 1)
    inorder(root)
    
    
    
    
