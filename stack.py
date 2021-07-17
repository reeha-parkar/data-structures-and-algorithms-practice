class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.root = None
        
    # Four main functions: push, pop, peek, and is_empty
    # push = pushes element into stack
    # pop = pops element out of the stack
    # peek = gives the top of the stack
    # is_empy = returns true if the stack is empty

    def is_empty(self):
        return True if self.root is None else False
    
    def push(self, new_data):
        # create new node
        new_node = Node(data=new_data)
        new_node.next = self.root
        self.root = new_node
        print("{} pushed into stack".format(new_data))

    def pop(self):
        if self.is_empty():
            print("Stack is empty, can't pop an empty stack")
            return
        if self.root:
            top = self.root
            self.root = self.root.next # assign root to next element
            popped = top.data
            print("{} popped out of the stack".format(popped))

    def peek(self):
        if self.is_empty():
            print("Empty stack")
            return
        
        print("{} is at the top of the stack".format(self.root.data))


if __name__=='__main__':
    stack = Stack()

    stack.pop()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.pop()
    stack.peek()
    stack.is_empty()

    


        
