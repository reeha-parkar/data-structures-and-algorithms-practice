class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def insert_at_end(self, new_data):
        # create new node
        new_node = Node(new_data)

        if self.head==None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def insert_at_nth(self, new_data, pos):
        # create new node
        new_node = Node(new_data)

        if pos==1:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        if current==None:
            print("Adding element at that position is not possible because")
            
        # run the loop for (pos-2) times to reach one node before the position
        for _ in range(1, pos-1): 
            current = current.next
        new_node.next = current.next
        current.next = new_node


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

    linked_list.insert_at_end(1)
    linked_list.insert_at_end(2)
    linked_list.insert_at_end(3)
    linked_list.insert_at_end(4)
    linked_list.insert_at_end(5)
    linked_list.insert_at_end(6)

    new_data = int(input("Enter the element"))
    position = int(input("Enter the position"))

    #insert(data, position)
    linked_list.insert_at_nth(new_data, position)
    linked_list.print_list()
    
    

    


    
