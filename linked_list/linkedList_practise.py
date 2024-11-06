# singly linked list
from turtledemo.penrose import start


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertion_at_the_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insertion_at_the_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        last_checked = self.head

        while last_checked.next:
            last_checked = last_checked.next

        last_checked.next = new_node



    def printing_list(self):
        if not self.head:
            print("LList is empty")
            return

        current_read = self.head
        while current_read:
            print(current_read.data, end=" -> ")
            current_read = current_read.next
        print("None")

        


llist = LinkedList()

llist.printing_list()
llist.insertion_at_the_beginning(1)
llist.insertion_at_the_end(10)
llist.insertion_at_the_beginning(12)
llist.printing_list()



