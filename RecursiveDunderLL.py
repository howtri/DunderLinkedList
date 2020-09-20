# Tristan Howell
# A small program which implements Linked List functionality via dunder methods using recursion


class Node:
    """
    Representation of a Node to be used from a linked list class
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class DunderLinkedList:
    """Recursive LL dunder implementation"""
    def __init__(self, data):
        """
        Initializes an empty linked list with no start node
        """
        self._head = None

    def __str__(self):
        pass

    def __add__(self, val):
        pass

    def __sub__(self, val):
        pass

    def __len__(self):
        pass

    def __contains__(self, item):
        pass

    def __delslice__(self, i, j):
        pass

    def __getitem__(self, item):
        pass