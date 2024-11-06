class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Reference to the next node
# LinkedList class manages the nodes and operations of the linked list
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize an empty linked list
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")
# Example usage:
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.print_list()