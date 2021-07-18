class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return True if self.front is None else False

    def enqueue(self, data):

        # create a queue node
        new_node = Node(data=data)

        if self.is_empty():
            self.front = new_node
            self.rear = new_node
            #print("{} added to the queue".format(data))
            return
        self.rear.next = new_node
        self.rear = new_node
        #print("{} added to the queue".format(data))

    
    def dequeue(self):

        if self.is_empty():
            #print("No queue to dequeue from")
            return

        frontmost_data = self.front.data
        self.front = self.front.next
        #print("{} has just been dequeued".format(frontmost_data))
        return frontmost_data

    def get_front(self):
        if self.is_empty():
            return
        return self.front.data

    def get_rear(self):
        if self.is_empty():
            return
        return self.rear.data
        
class Stack:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()


    # making push operation costly
    def push(self, data):
        self.queue1.enqueue(data)
        print("{} just pushed into stack".format(data))
            
    def get_size(self):
        size = 0
        if self.queue1.is_empty():
            return
        current = self.queue1.front
        while current!=None:
            current = current.next
            size += 1
        return size

    def pop(self):
        if self.queue1.is_empty():
            return
        
        for _ in range(0, self.get_size()-1):
            self.queue2.enqueue(self.queue1.get_front())
            self.queue1.dequeue()
        popped_data = self.queue1.get_front()
        self.queue1.dequeue()
        self.queue1, self.queue2 = self.queue2, self.queue1
        print("{} just popped out of stack".format(popped_data))
            
    

    def peek(self):
        if self.queue1.is_empty():
            print("Empty stack")
            return
        print("{} is at the top of the stack".format(self.queue1.get_rear()))

        
    
if __name__ == '__main__':

    stack = Stack()

    stack.push(1)
    stack.peek()
    print("SIZE=",stack.get_size())
    stack.push(2)
    print("SIZE=",stack.get_size())
    stack.peek()
    stack.push(3)

    print("SIZE=",stack.get_size())
    stack.peek()
    stack.pop()
    print("SIZE=",stack.get_size())
    stack.peek()
    stack.push(5)
    print("SIZE=",stack.get_size())
    stack.peek()

    


    
