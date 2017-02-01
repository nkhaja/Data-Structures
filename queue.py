#!python

from linkedlist import LinkedList
class Queue(LinkedList):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any"""

        super(Queue, self).__init__()
        if iterable:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue"""
        return 'Queue({})'.format(self.length())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise"""
        return super(Queue, self).is_empty()


    def length(self):
        """Return the number of items in this queue"""
        return super(Queue, self).length()


    def peek(self):
        """Return the next item in this queue without removing it,
        or None if this queue is empty"""
        if self.is_empty():
            return None

        else:
            return self.tail.data


    def enqueue(self, item):
        """Enqueue the given item into this queue"""
        super(Queue, self).prepend(item)


    def dequeue(self):
        """Return the next item and remove it from this queue,
        or raise ValueError if this queue is empty"""
        if self.is_empty():
            raise ValueError

        dequeued_item = self.tail.data
        super(Queue, self).delete(self.tail.data)
        return dequeued_item
