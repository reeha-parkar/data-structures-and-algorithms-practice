class Node:
    def __init__(self, next=None, prev=None, data=None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current = self.head

        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def add_at_front(self, new_data):
        print("Adding {} at front".format(new_data))
        new_node = Node(data=new_data)
        new_node.next = self.head
        new_node.prev = None

        if self.head:
            self.head.prev = new_node

        self.head = new_node

    def add_at_end(self, new_data):
        print("Adding {} at end".format(new_data))
        new_node = Node(data=new_data)
        new_node.next = None
        new_node.prev = None # will change

        current = self.head

        if self.head is None:
            self.head = new_node
            return
                
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
        

if __name__ == '__main__':
    dll = LinkedList()

    dll.add_at_end(1)
    dll.print_list()
    dll.add_at_end(2)
    dll.print_list()
    dll.add_at_end(4)
    dll.print_list()
    dll.add_at_end(6)
    dll.print_list()
    dll.add_at_end(33)
    dll.print_list()
    dll.add_at_front(45)
    dll.print_list()
    dll.add_at_front(34)
    dll.print_list()
    dll.add_at_front(3)

    dll.print_list()
    
