class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # enqueue, dequeue, and is_empty functions
    # you enqueue from the rear end, and dequeue from the front

    def is_empty(self):
        return self.front==None

    def enqueue(self, new_data):
        #create new node
        new_node = Node(data=new_data)

        if self.rear==None:
            self.front = self.rear = new_node
            print("{} added to the queue".format(new_data))
            return

        self.rear.next = new_node
        self.rear = new_node
        print("{} added to the queue".format(new_data))


    def dequeue(self):

        
        if self.is_empty():
            print("No queue to dequeue from")
            return

        if self.front==self.rear:
            self.front = self.rear = None
        
        frontmost = self.front
        self.front = frontmost.next
        
        print("{} has just been dequeued".format(frontmost.data))
            



if __name__ == '__main__':
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(6)
    queue.dequeue()
    queue.dequeue()
    print(queue.front.data)
    print(queue.rear.data)

    

    
