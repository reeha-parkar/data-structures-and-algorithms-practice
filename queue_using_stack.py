class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return True if self.root is None else False

    def push(self, data):
        # create a new stack node
        new_node = Node(data=data)
        new_node.next = self.root
        self.root = new_node
        #print("{} popped into stack".format(data))

    def pop(self):
        if self.is_empty():
            #print("Stack is empty, can't pop")
            return

        if self.root:
            top = self.root
            top_data = top.data
            self.root = top.next
            return top_data
            #print("{} popped out of the stack".format(top_data))

    def peek(self):
        if self.is_empty():
            print("Empty stack")
            return
        #print("The top of the stack is {}".format(self.root.data))

    def get_size(self):
        if self.is_empty():
            print("Empty stack")
            return
        current = self.root
        count = 1
        while current.next:
            current = current.next
            count += 1
        #print("The number of elements in stack are {}".format(count))

class Queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, data):
        self.stack1.push(data)
        print("{} is enqueued".format(data))
        
    # implement by making dequeue operation costly
    def dequeue(self):
        if self.stack1.is_empty() and self.stack2.is_empty():
            print("Queue is empty")
            return

        elif self.stack1.is_empty()==False and self.stack2.is_empty():
            while self.stack1.is_empty()==False:
                current = self.stack1.pop()
                self.stack2.push(current)
            print("{} is dequeued".format(self.stack2.pop()))
            return
        else:
            print("{} is dequeued".format(self.stack2.pop()))


if __name__=='__main__':

    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.dequeue()
    queue.dequeue()
