##singular linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

    def print_ll(self):
        current = self.head

        while current:
            print(current.data, end=' --> ')
            current = current.next
        print("None")

ll1 = LinkedList()

ll1.append(1)
ll1.append(2)
ll1.print_ll()