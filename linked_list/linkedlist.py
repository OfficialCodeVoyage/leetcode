from debugpy.common.timestamp import current


class Node:
    def __init__(self, hold_value):

        self.data = hold_value ##Data field
        self.next = None ##next mode

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data) # calling Node class with passing data

        if self.head is None: # if empty, setting up a head llist
            self.head = new_node
        else: ## when the List Isn't Empty
            last = self.head # We need to find the last node in the list (the one where next is None). So we start at the head (the first node).
            while last.next: # loop to keep moving to the next node, while not finding None node
                last = last.next
            last.next = new_node

    def print(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def lenght(self):
        current = self.head
        counter = 0

        while current:
            counter += 1
            current = current.next
        return counter

    def searchforvalue(self, value):
        current = self.head

        while current:
            if current.data == value:
                return "Found"
            else:
                current = current.next
        return "Not found"

    def insertatthebeginning(self, value):
        insert_node = Node(value)

        if self.head is None:
            self.head = insert_node
        else:
            insert_node.next = self.head
            self.head = insert_node




ll = LinkedList()
ll.append(5)
ll.insertatthebeginning(1)
ll.append(10)
ll.print()

