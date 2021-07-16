class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def print_list(self):
        current = self.head
        while(current):
            print(current.data, end=' ')
            current = current.next

if __name__=='__main__':

    linked_list = LinkedList()

    linked_list.head = Node(1)
    second = Node(2)
    third = Node(3)
    
    second.next = third
    linked_list.head.next = second
    #next of third is already None

    linked_list.print_list()

