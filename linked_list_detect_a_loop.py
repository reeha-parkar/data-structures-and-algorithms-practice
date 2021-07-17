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

    # Floyd's Cycle Finding Algorithm
    # Time complexity: O(n)
    # Space complexity: O(1) since no auxiliary space used
    def detect_loop(self):
        slow = self.head
        fast = self.head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                return True
        return False

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

    # Adding a loop
    linked_list.head.next.next = linked_list.head.next

    if linked_list.detect_loop():
        print("Loop detected")
    else:
        print("There is no loop")

    

    
