class Node:
    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = [data]
        self.left = None
        self.middle = None
        self.right = None

    def add(self, item):
        if len(self.data) == 2:
            if item < self.data[0]:
                removed = self.data[0]
                self.data[0] = item
                return removed
            elif item > self.data[1]:
                removed = self.data[1]
                self.data[1] = item
                return removed
            else:
                return item
        elif len(self.data) == 1:
            if item < self.data[0]:
                self.data.append(self.data[0])
                self.data[0] = item
            else:
                self.data.append(item)
        else:
            self.data.append(item)






class TwoThreeTree:
    def __init__(self,iterable=None):
        self.root = None
        if iterable:
            for item in iterable:
                self.insert(item)


def search(self, item):

    current_node = self.rooot

    while current_node is not None:
        if item in current_node.data:
            return True

        elif item < current_node.data[0]:
            current_node = current_node.left

        elif len(current_node.data) == 1:
            current_node = current_node.right

        else:
            if item > current_node.data[1]:
                current_node = current_node.right
            else:
                current_node = current_node.middle

    return False

def insert_helper(self, item):
    pass

def insert(self, item, node=None):
    if node == None:
        node = self.root

    if len(node.data) < 2:
        node.add(item)

    else:
        
