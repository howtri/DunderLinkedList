# Tristan Howell
# Not dunder yet but a recursive LL implementation



class Node:
    """
    Representation of a Node to be used from a linked list class
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    A linked list implementation of the list ADT, all functions except for get_head are implemented recursively.
    Implementation allows for adding and removing nodes. Additionally checking if a value is contained, inserting a
    value, reversing the linked list, and outputting as a standard Python list
    """
    def __init__(self):
        """
        Initializes an empty linked list with no start node
        """
        self._head = None

    def get_head(self):
        """
        Returns node object from head
        """
        return self._head

    def add(self, val, current=None):
        """
        Adds a node with data as val to the linked list, current variable is used solely for recursive calls
        """
        # Case of empty list
        if self._head is None:
            self._head = Node(val)
            return

        # For the first call of add we set current to head
        if current is None:
            current = self._head

        # Until we reach a node with no next, we recall add
        if current.next is None:
            current.next = Node(val)
        else:
            self.add(val, current.next)

    def remove(self, val, previous=None, current=1):
        """
        Removes the node containing val from the linked list by tracking a previous and current, progresses
        through the list until the nodes data = val and sets the previous nodes next to skip our current

        Default for current is 1 due to checking if current is not None to determine our number of recursive calls
        """
        # Case of empty list
        if self._head is None:
            return

        # for first time being called
        if current == 1:
            current = self._head

        # in the case that head must be removed
        if self._head.data == val:
            self._head = self._head.next
            return

        if current is not None and current.data != val:
            return self.remove(val, current, current.next)
        # for the last value, throws error if not checking if current is not none
        elif current is not None:
            previous.next = current.next
        else:
            previous.next = None

    def contains(self, val, current=None):
        """
        Recursively checks if a value is contained within one of the nodes of the linked list returning True if found
        """
        # In the case of empty linked list
        if self._head is None:
            return False

        # For our initial function call we set currents place
        if current is None:
            current = self._head

        # iterate over entire list and return True if a nodes value is equal the passed val
        if current.data == val:
            return True
        # we only continue if the next node contains
        elif current.next is not None:
            return self.contains(val, current.next)

        # entire list checked and val not found
        return False

    def insert(self, val, position, previous=None, current=1, cur_pos=0):
        """
        Removes the node containing val from the linked list

        Default for current is 1 due to checking if current is not None to determine our number of recursive calls
        """
        # case of empty list
        if self._head is None:
            self._head = Node(val)
            return

        # for first time being called
        if current == 1:
            current = self._head

        # inserting at the start of the list
        if position == 0:
            self._head = Node(val)
            self._head.next = current
            return

        if current is not None and cur_pos != position:
            # iterate while list continues and we're not at the position to insert
            return self.insert(val, position, current, current.next, cur_pos+1)
        # if a position is greater or equal the length of the list it is just appended to the end
        else:
            previous.next = Node(val)
            previous.next.next = current

    def reverse(self, previous=None, current=1):
        """
        Reverses our linked list by iterating through the entire list and once reaching the end, setting head to our
        end position and as we exit our recursive calls setting the stored previous nodes to our current.next

        Default for current is 1 due to checking if current is not None to determine our number of recursive calls
        """
        # in the case of an empty list
        if self._head is None:
            return

        # for our first call we set our current position
        if current == 1:
            current = self._head

        # iterate through the entire list passing a previous a previous and current relative to the next position
        if current.next is not None:
            # note we don't return self.reverse as we need to continue the function as we break out of
            # each successive recursive call
            self.reverse(current, current.next)
        # once we reach the last node this is our new head
        else:
            self._head = current

        # as the recursive calls complete from end to start we change the nexts to our previous nodes
        if previous is not None:
            current.next = previous
        # once all are reversed our initial head value should not point to None as next
        else:
            current.next = None

    def to_regular_list(self, current=1, reg_list=None):
        """
        Recursively reads every value from the linked list and appends to a standard python list

        Default for current is 1 due to checking if current is not None to determine our number of recursive calls
        """
        # Returns empty python list if linked list is empty
        if self._head is None:
            return []

        # Initializes our list and current position for first call
        if current == 1:
            current = self._head
            reg_list = []

        # until we reach an empty node we append to our list
        if current is None:
            return reg_list
        else:
            reg_list.append(current.data)
            return self.to_regular_list(current.next, reg_list)
