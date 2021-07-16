class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, new_data):
        # create new node
        new_node = Node(new_data)

        new_node.next = self.head

        self.head = new_node


    def print_list(self):
        current = self.head
        if current==None:
            print("The list is empty")
        else:
            while current!=None:
                print(current.data, end=' ')
                current = current.next
            print()

if __name__=='__main__':

    linked_list = LinkedList()

    linked_list.insert_at_start(1)
    linked_list.print_list()

    linked_list.insert_at_start(2)
    linked_list.print_list()

    linked_list.insert_at_start(3)
    linked_list.print_list()

    
