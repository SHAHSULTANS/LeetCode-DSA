from numpy import size


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, data):
        new_node = Node(data)

        if not self.head:  # If the list is empty
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node  # Link the new node
        self.tail = new_node  # Update the tail to the new node

    def display_all_nodes(self):
        if not self.head:  # If the list is empty
            print("There is no existing node")
            return

        current = self.head
        while current:  # Traverse through all nodes
            print(current.data, end=" -> ")
            current = current.next

        print("None")  # Indicate the end of the list


# Test the linked list
singly_link_list = SinglyLinkedList()

singly_link_list.add_node(5)
singly_link_list.add_node(4)
singly_link_list.add_node(10)
singly_link_list.add_node(50)

singly_link_list.display_all_nodes()
print(size(singly_link_list))