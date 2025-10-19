class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_after_value(self, target, data):
        current = self.head
        while current:
            if current.data == target:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print(f"Value '{target}' not found in the list.")

    def remove_value(self, target):
        current = self.head
        if not current:
            return

        if current.data == target:
            self.head = current.next
            return

        while current.next:
            if current.next.data == target:
                current.next = current.next.next
                return
            current = current.next
        print(f"Value '{target}' not found in the list.")

    def print_list(self):
        current = self.head
        if not current:
            print("List is empty.")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("X")
    
    #Activity A.
    def remove_beginning(self):
        if self.head is None:
            return None 
        removed_data = self.head.data
        self.head = self.head.next  
        return removed_data
    
    #Activity B.
    #Acitivity C.