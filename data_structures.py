class SimpleArray:
    """Basic wrapper around Python list to demonstrate array operations."""

    def __init__(self):
        self.items = []

    def insert_end(self, value):
        self.items.append(value)

    def insert_at_index(self, index, value):
        if index < 0 or index > len(self.items):
            raise IndexError("Index out of bounds.")
        self.items.insert(index, value)

    def delete_by_index(self, index):
        if index < 0 or index >= len(self.items):
            raise IndexError("Index out of bounds.")
        return self.items.pop(index)

    def access(self, index):
        if index < 0 or index >= len(self.items):
            raise IndexError("Index out of bounds.")
        return self.items[index]

    def display(self):
        return self.items[:]


class Stack:
    """Stack implementation using a Python list."""

    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from empty stack.")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty.")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def display(self):
        return self.items[:]


class Queue:
    """Queue implementation using a Python list."""

    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Cannot dequeue from empty queue.")
        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def display(self):
        return self.items[:]


class ListNode:
    """Node for singly linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    """Singly linked list implementation."""

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, value):
        new_node = ListNode(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, value):
        new_node = ListNode(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def delete_value(self, value):
        if self.head is None:
            return False

        if self.head.data == value:
            self.head = self.head.next
            return True

        previous = self.head
        current = self.head.next

        while current:
            if current.data == value:
                previous.next = current.next
                return True
            previous = current
            current = current.next

        return False

    def traverse(self):
        values = []
        current = self.head

        while current:
            values.append(current.data)
            current = current.next

        return values


def demonstrate_data_structures():
    print("----- Array Demo -----")
    arr = SimpleArray()
    arr.insert_end(10)
    arr.insert_end(20)
    arr.insert_at_index(1, 15)
    print("Array contents:", arr.display())
    print("Access index 1:", arr.access(1))
    arr.delete_by_index(0)
    print("After deletion:", arr.display())

    print("\n----- Stack Demo -----")
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Stack contents:", stack.display())
    print("Top element:", stack.peek())
    print("Popped:", stack.pop())
    print("After pop:", stack.display())

    print("\n----- Queue Demo -----")
    queue = Queue()
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")
    print("Queue contents:", queue.display())
    print("Front element:", queue.front())
    print("Dequeued:", queue.dequeue())
    print("After dequeue:", queue.display())

    print("\n----- Linked List Demo -----")
    linked_list = SinglyLinkedList()
    linked_list.insert_at_end(100)
    linked_list.insert_at_end(200)
    linked_list.insert_at_beginning(50)
    print("Linked list traversal:", linked_list.traverse())
    linked_list.delete_value(200)
    print("After deletion:", linked_list.traverse())


if __name__ == "__main__":
    demonstrate_data_structures()