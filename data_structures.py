class Node:
    """
    A node stores the item of the element in the linked-list as well as
    keeps a pointer to the next node.
    """

    def __init__(self, item, next):
        self.item = item
        self.next = next


class Stack:
    """
    Stack implemented using linked list.
    Last in first out (LIFO).
    """
    def __init__(self, head=None):

        self.head = head # Pointer to first (last inserted) element

    def pop(self):
        """
        Removes and returns the last added element
        """

        if not self.head:
            raise ValueError("List is empty")

        # FIXME: This is the mistake! It should return the item of the head node!
        item = self.head.next.item

        self.head = self.head.next

        return item

    def push(self, new_item):
        """
        Push new item to stack
        """

        self.head = Node(item=new_item, next=self.head)
