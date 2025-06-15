class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def print_list(self):
        if not self.head:
            print("List is empty.")
            return
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

    def delete_nth_node(self, n):
        if not self.head:
            raise Exception("Cannot delete from an empty list.")
        if n <= 0:
            raise IndexError("Index must be 1 or greater.")
        if n == 1:
            print(f"Deleting node at position {n} with value {self.head.data}")
            self.head = self.head.next
            return
        curr = self.head
        count = 1
        while curr and count < n - 1:
            curr = curr.next
            count += 1
        if not curr or not curr.next:
            raise IndexError("Index out of range.")
        print(f"Deleting node at position {n} with value {curr.next.data}")
        curr.next = curr.next.next

if __name__ == "__main__":
    ll = LinkedList()
    ll.add_node(10)
    ll.add_node(20)
    ll.add_node(30)
    ll.add_node(40)
    print("Initial List:")
    ll.print_list()
    try:
        ll.delete_nth_node(2)
        print("\nList after deleting 2nd node:")
        ll.print_list()
    except Exception as e:
        print(f"Error: {e}")
    try:
        ll.delete_nth_node(10)
    except Exception as e:
        print(f"\nError: {e}")
    try:
        ll.head = None
        ll.delete_nth_node(1)
    except Exception as e:
        print(f"\nError: {e}")