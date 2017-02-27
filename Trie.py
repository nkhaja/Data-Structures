class Tnode:
    def __init__(self, data=None):
        self.data = data
        self.subs = {} # dict of nodes
        self.terminal = False

    def insert(self, item, index=0):
        next_node = None
        print item

        if len(item) < 1:
            return

        try:
            # subItem exists at a child node
            next_node = self.subs[item]

        # need to add node for subItem
        except KeyError:
            next_node = Tnode(item[index])
            self.subs[item[index]] = next_node

        index += 1

        # have we reached the end of item?
        if index == len(item):
            next_node.terminal = True
            return
        else:
            print('exploring next node')
            next_node.insert(item, index)




    def has_item(self, item, index=0):
        next_node = None

        if len(item) < 1:
            return True

        try:
            # does this level have the subitem we want?
            next_node = self.subs[item[index]]
            index += 1

            if index == len(item):
                # If terminated here before word exists
                # else this is a subword that matches serendipitously
                return next_node.terminal
            else:
                return next_node.has_item(item, index)

        except KeyError:
            return False

    def remove_item(self, item, index=0):
        next_node = None

        if len(item) < 1:
            return

        try:
            # does this level have the subitem we want?
            next_node = self.subs[item[index]]
            index += 1

            #if we're at the end of the word, delete the path to this node
            if index == len(item) and next_node.terminal:
                del self.subs[item[index]]
                return
            # continue down the Trie
            else:
                next_node.has_item(item, index)

        except KeyError:
            # This word does not exist in the Trie
            return ValueError





class Trie(object):
    """A trie is tree with an arbitrary number of branches for each child.
    Typical use cases are auto-correct and checking phone numbers"""

    def __init__(self,iterable=None):
        """Initialize this min heap with an empty list of items"""

        self.root = Tnode()

        if iterable is not None:
            for item in iterable:
                self.root.insert(item)

    def insert_item(self, item):
        self.root.insert(item)

    def has_item(self, item):
        return self.root.has_item(item)

    def remove_item(self, item):
        self.root.delete(item)

if __name__ == "__main__":
    trie = Trie(["string"])
    print trie.has_item("string")
