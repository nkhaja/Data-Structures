#!python
from linkedlist import LinkedList
class Stack(LinkedList):


    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any"""
        super(Stack, self).__init__()
        # TODO: initialize instance variables
        pass
        if iterable:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack"""
        return 'Stack({})'.format(self.length())

    #01
    def is_empty(self):
        """Return True if this stack is empty, or False otherwise"""
        return super(Stack, self).is_empty()


    #0n or O1 dep on implementation
    def length(self):
        """Return the number of items in this stack"""
        return super(Stack, self).length()

    #O1
    def peek(self):
        """Return the top item on this stack without removing it,
        or None if this stack is empty"""
        if self.is_empty():
            return None
        else:
            return self.head.data

    #01
    def push(self, item):
        """Push the given item onto this stack"""
        # TODO: push given item
        super(Stack,self).prepend(item)

    #01
    def pop(self):
        """Return the top item and remove it from this stack,
        or raise ValueError if this stack is empty"""
        if self.is_empty():
            raise ValueError

        popped_item = self.head.data
        super(Stack,self).delete(self.head.data)
        return popped_item
