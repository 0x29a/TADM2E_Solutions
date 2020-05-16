class Node:
    """
    Node of linked list.
    """

    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, value):
        if not self.head:
            self.head = Node(value)
            self.tail = self.head
        else:
            node = Node(value)
            self.tail.next = node
            self.tail = node

    def print_list(self):
        current_node = self.head

        print("head ->")
        while current_node is not None:
            print(current_node.value)

            current_node = current_node.next

            print("->")

        print("tail")

    def reverse_list(self):
        """
        Pretty complicated.

        Let's suppose we have list:
        A (head) -> B -> C -> D -> None

        After first iteration we have:
        B -> A (head) -> C -> D -> None

        Second:
        C -> B -> A (head) -> D -> None

        Third:
        D (head) -> C -> B -> A -> None

        This reverse has O(n) complexity.
        """
        current_head = self.head
        head = self.head

        while current_head is not None:
            temp = current_head
            current_head = self.head.next
            temp_next = current_head.next
            head.next = temp_next
            current_head.next = temp

            if head.next is None:
                self.head = current_head
                break


def main():
    linked_list = LinkedList()

    for value in range(20):
        linked_list.add_node(value)

    linked_list.print_list()

    linked_list.reverse_list()

    linked_list.print_list()


if __name__ == "__main__":
    main()
