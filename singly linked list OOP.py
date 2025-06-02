class Node:
    """Represents a single node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Manages a singly linked list using head pointer."""
    def __init__(self):
        self.head = None

    def add_node(self, data):
        """Adds a node to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        """Prints all elements in the list."""
        if not self.head:
            print("List is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        """Deletes the nth node from the list (1-based index)."""
        if not self.head:
            raise Exception("Cannot delete from an empty list.")

        if n <= 0:
            raise IndexError("Index must be a positive integer.")

        if n == 1:
            deleted_data = self.head.data
            self.head = self.head.next
            print(f"Deleted node at index {n}: {deleted_data}")
            return

        current = self.head
        count = 1
        while current and count < n - 1:
            current = current.next
            count += 1

        if not current or not current.next:
            raise IndexError("Index out of range.")

        deleted_data = current.next.data
        current.next = current.next.next
        print(f"Deleted node at index {n}: {deleted_data}")


# Testing the implementation
if __name__ == "__main__":
    ll = LinkedList()

    # Add sample nodes
    ll.add_node(10)
    ll.add_node(20)
    ll.add_node(30)
    ll.add_node(40)

    print("Initial List:")
    ll.print_list()

    # Delete 3rd node
    try:
        ll.delete_nth_node(3)
    except Exception as e:
        print("Error:", e)

    print("\nList after deleting 3rd node:")
    ll.print_list()

    # Delete 1st node
    try:
        ll.delete_nth_node(1)
    except Exception as e:
        print("Error:", e)

    print("\nList after deleting 1st node:")
    ll.print_list()

    # Try deleting with index out of range
    try:
        ll.delete_nth_node(10)
    except Exception as e:
        print("Error:", e)

    # Try deleting from an empty list
    empty_list = LinkedList()
    try:
        empty_list.delete_nth_node(1)
    except Exception as e:
        print("Error:", e)
