# Tristan Howell
# A small program which implements Linked List functionality via dunder methods


class Node:
    """
    Representation of a Node to be used from a linked list class
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class DunderLinkedList:
    """LL dunder implementation"""
    def __init__(self):
        """Initializes an empty linked list with no start node"""
        self._head = None

    def __str__(self):
        """Prints its a LL and number of nodes, would be nice to show or return a regular python list also"""
        return f'Linked list consisting of {len(self)} nodes'

    def __add__(self, val):
        """Adds a node to the end of the LL"""
        if self._head == None:
            self._head = Node(val)
        else:
            current = self._head
            while current.next:
                current = current.next
            current.next = Node(val)

    def __sub__(self, val):
        """
        Removes the first instance of a value in LL
        """
        try:
            # if the val to remove is the first node or the list is one long
            current = self._head
            if val == current.data:
                if self._head.next:
                    self._head = self._head.next
                    return True
                else:
                    self._head = None
                    return True

            while current.next:
                if val == current.data:
                    previous.next = current.next
                    return True
                previous = current
                current = current.next

            # if val corresponds to last node
            if val == current.data:
                previous.next = None
                return True
            return False

        except AttributeError:
            print('Linked List has no nodes! Add to it first.')
            return False

    def __len__(self):
        """Returns the number of nodes in LL"""
        try:
            current = self._head
            count = 1
            while current.next:
                current = current.next
                count += 1
            return count

        except AttributeError:
            return 0

    def __contains__(self, val):
        """Returns true if the passed val is found in the LL"""
        try:
            current = self._head
            while current.next:
                if val == current.data:
                    return True
                current = current.next

            if val == current.data:
                return True
            return False

        except AttributeError:
            return False

    def __getitem__(self, index):
        """
        Allow for built in python slicing to retrieve a nodes value
        """
        # for reverse indexing (-1 is last etc)
        if index < 0:
            index = len(self) + index
        try:
            count = 0
            current = self._head
            while current.next:
                if count == index:
                    return current.data
                current = current.next
                count += 1

            if count == index:
                return current.data
            return False

        except AttributeError:
            print('Linked List has no nodes! Add to it first.')
            return False

    def __setitem__(self, index, value):
        """Allows changing a nodes data by index. Ex: LL[1] = 'hello'"""
        # for reverse indexing (-1 is last etc)
        if index < 0:
            index = len(self) + index
        try:
            count = 0
            current = self._head
            while current.next:
                if count == index:
                    current.data = value
                    return True
                current = current.next
                count += 1

            if count == index:
                current.data = value
                return True
            return False

        except AttributeError:
            print('Linked List has no nodes! Add to it first.')
            return False


d1 = DunderLinkedList()
d1 + 7
d1 + 2
d1 + 3
d1 - 3
print(d1[-1])
d1[-1] = 3
print(3 in d1)
print(d1)