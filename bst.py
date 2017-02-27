#!python

class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.left = None
        self.right = None

    def has_children(self):
        if self.left == None and self.right == None:
            return False
        else:
            return True


    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))


class Bst(object):

    def __init__(self, iterable=None):
        self.root = None
        self.size = 0

        if iterable:
            for item in iterable:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this linked list"""
        return 'Bst({})'.format(self.as_list())

    def _len_(self):
        return self.size

    def insert(self, item):
        if self.root == None:
            self.root = Node(item)
            self.size += 1
            return

        prev_node = None
        current_node = self.root
        while current_node is not None:
            if current_node.data > item:
                prev_node = current_node
                current_node = current_node.left

            else:
                prev_node = current_node
                current_node = current_node.right


        if prev_node.data > item:
            prev_node.left = Node(item)
        else:
            prev_node.right = Node(item)
        self.size += 1



    def delete(self, item):

        # Item doesn't exist in Tree
        if self.root == None:
            raise ValueError

        #Item is Root, replace root
        if self.root.data == item:
            new_root = self.replace_node(self.root)
            if new_root is not None:
                print 'root is not none'

                #new Root adopts old root's children
                new_root.left = self.root.left
                new_root.right = self.root.right

                #remove old root's children
                self.root.right = None
                self.root.left = None
                self.root = new_root
                return
            else:
                print 'root is none'
                #root was only node in tree
                self.root = None
            self.size -= 1
            return

        if not self.root.has_children:
            raise ValueError

        #looking for non-root node
        prev_node = self.root
        current_node = None

        if item > self.root.data:
            current_node = self.root.right
        else:
            current_node = self.root.left

        while current_node is not None:
            # desired value found
            if current_node.data == item:
                self.size -= 1
                new_node = self.replace_node(current_node)

                #node being replaced was a right child
                if current_node.data > prev_node.data:
                    prev_node.right = new_node

                #node being replaced was a left child
                else:
                    prev_node.left = new_node

                #new node does not have children
                if new_node is None:
                    return

                #need to assign replaced node's children
                #to new nodes
                else:
                    new_node.left = current_node.left
                    new_node.right = current_node.right

            #keep looking for new node
            else:
                prev_node = current_node
                if item > current_node.data:
                    current_node = current_node.right
                else:
                    current_node = current_node.left
        raise ValueError


    def replace_node(self, node):
        if not node.has_children:
            print 'no children'
            return None
        if node.left and not node.right:
            return node.left
        elif node.right and not node.left:
            return node.right
        else:
            print 'finding replacement'
            return self.find_replacement(node, True)


    #this function is called only if given node has two children
    def find_replacement(self, node, predecessor):
        target = None
        if predecessor:
            target = node.left
        else:
            target = node.right

        if not target.has_children:
            return target

        prev_node = node
        current_node = target



        if predecessor:
            while current_node.right is not None:
                print 'entered loop'
                prev_node = current_node
                current_node = current_node.right

            if current_node == node:
                print 'node'
                return current_node

            elif current_node.left is not None:
                prev_node.right = current_node.left
                current_node.left = None
                print 'promoted left'
                return current_node

            else:
                print 'returning at end'
                print current_node
                return current_node



    def find_child_of(node, smallest):
        if not node.has_children():
            return node

        prev_node = None
        current_node = node
        while current_node is not None:
            prev_node = current_node
            if smallest:
                current_node = current_node.left
            else:
                current_node = current_node.right

        if current_node.right:
            found = current_node.right
            current_node.right = None
            return found

        elif current_node.left:
            found = current_node.left
            current_node.left = None
            return found

        else:
            return current_node

        return current_node


    def search_iterative(self, item):
        current_node = self.root

        while current_node is not None:
            if current_node.data == item:
                return True

            elif current_node.data > item:
                current_node = current_node.left
            else: #current_node.data < item:
                current_node = current_node.right

        return False


    #implement with a retrieve function
    def search_recursive(self,item, node):

        if node == None:
            return False

        elif node.data == item:
            return True

        elif node.data > item:
            return self.search_recursive(item, node.left)

        else:
            return self.search_recursive(item, node.right)

    def in_order(self, node, output=[]):

        #left,visit, right
        if node.left is not None:
            self.in_order(node.left, output)

        output.append(node.data)

        if node.right is not None:
            self.in_order(node.right, output)

        return output

    def post_order(self, node):
        if node == None:
            return

        post_order(self, node.left)
        post_order(self, node.right)
        print(node.data)

    def pre_order(self, node):

        if node == None:
            return

        print(node.data)
        pre_order(self, node.left)
        pre_order(self, node.right)


    def get_extreme_for_node(self, get_max, node):
        prev_node = None
        current_node = node
        while current_node is not None:
            prev_node = current_node
            if get_max:
                current_node = current_node.right
            else:
                current_node = current_node.left
        return prev_node.data

    def get_extreme(self, get_max):
        return self.get_extreme_for_node(get_max, self.root)
