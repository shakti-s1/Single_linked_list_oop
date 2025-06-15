# linked_list.py

# This file implements a Singly Linked List in Python using Object-Oriented Programming principles.
# Author: Shakti Singh

class Node:
    """
    This class represents a single node in a linked list.
    Each node stores data and a reference to the next node.
    """
    def __init__(self, data):
        self.data = data  # Store the actual value
        self.next = None  # Pointer to the next node (default is None)


class LinkedList:
    """
    This class manages the linked list and provides methods to manipulate it.
    """
    def __init__(self):
        self.head = None  # The head of the list (initially empty)

    def add_node(self, data):
        """
        Adds a new node with the given data at the end of the list.
        """
        new_node = Node(data)

        # If the list is empty, the new node becomes the head
        if self.head is None:
            self.head = new_node
        else:
            # Traverse to the end of the list and attach the new node
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_list(self):
        """
        Prints all the elements in the linked list.
        """
        if self.head is None:
            print("The list is empty.")
            return

        print("Linked List:", end=" ")
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        """
        Deletes the nth node in the linked list (1-based index).
        Handles exceptions for edge cases.
        """
        if self.head is None:
            raise Exception("Cannot delete from an empty list.")

        if n <= 0:
            raise Exception("Invalid index. Index must be 1 or greater.")

        # Special case: delete the head
        if n == 1:
            deleted_data = self.head.data
            self.head = self.head.next
            print(f"Deleted node at position 1 with data: {deleted_data}")
            return

        current = self.head
        count = 1

        # Traverse to (n-1)th node
        while current and count < n - 1:
            current = current.next
            count += 1

        # If n is out of range
        if current is None or current.next is None:
            raise Exception("Index out of range. Cannot delete.")

        deleted_data = current.next.data
        current.next = current.next.next
        print(f"Deleted node at position {n} with data: {deleted_data}")


# ------------------------------
# Test Code (Runs only when file is executed directly)
# ------------------------------

if __name__ == "__main__":
    # Create a new linked list
    my_list = LinkedList()

    # Add nodes to the list
    my_list.add_node(10)
    my_list.add_node(20)
    my_list.add_node(30)
    my_list.add_node(40)

    # Print the original list
    print("Original List:")
    my_list.print_list()

    # Try deleting the 2nd node
    try:
        my_list.delete_nth_node(2)
    except Exception as e:
        print("Error:", e)

    # Print the updated list
    print("\nList after deleting 2nd node:")
    my_list.print_list()

    # Try deleting with an invalid index
    try:
        my_list.delete_nth_node(10)
    except Exception as e:
        print("Error:", e)
