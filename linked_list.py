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

#--- Activity  ---

    #Activity A.
    def remove_beginning(self):
        if self.head is None:
            return None 
        removed_data = self.head.data
        self.head = self.head.next  
        return removed_data
    
    #Activity B.
    def remove_at_end(self):
        if self.head is None:
            return None  
        if self.head.next is None:
            removed_data = self.head.data
            self.head = None  
            return removed_data
        tigatalon = self.head
        while tigatalon.next.next:
            tigatalon = tigatalon.next
        removed_data = tigatalon.next.data
        tigatalon.next = None  
        return removed_data
    
    #Acitivity C.
    def remove_at(self, data):
        if self.head is None:
            return None 

    
        if self.head.data == data:
            removed_data = self.head.data
            self.head = self.head.next
            return removed_data


        tigatalon = self.head
        while tigatalon.next:
            if tigatalon.next.data == data:
                removed_data = tigatalon.next.data
                tigatalon.next = tigatalon.next.next 
            tigatalon = tigatalon.next

        return None

            