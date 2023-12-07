"""
You're given a Linked List with at least one node. Write a function that returns the middle node of the Linked List.

"""


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middle_node(linked_list):
    """
    Complexity:

    Time: O(n)
    Space: O(1)
    """
    slow_pointer = linked_list
    fast_pointer = linked_list
    while fast_pointer is not None and fast_pointer.next is not None:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

    return slow_pointer
