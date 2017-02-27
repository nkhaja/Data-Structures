#!python

from bst import Bst, Node
import unittest

class NodeTest(unittest.TestCase):
    def test_init(self):
        data = 'nabil'
        node = Node('nabil')
        assert node.data == data
        assert node.left == None
        assert node.right == None

    def test_has_children(self):
        node = Node('grandparent')
        print node.left
        print node.right
        assert node.has_children() == False

        node.left = Node('mom')
        node.right = Node('uncle')
        assert node.has_children() == True
        assert node.left.data == 'mom'
        assert node.right.data == 'uncle'



class BstTest (unittest.TestCase):
    def test_init(self):
        bst = Bst([5,6,1,2,8,3])
        assert bst.root.data == 5
        assert bst.root.left.data == 1
        assert bst.root.right.data == 6
        assert bst.size == 6

    def test_insert(self):
        bst = Bst()
        bst.insert(10)
        bst.insert(3)
        bst.insert(4)
        bst.insert(1)
        bst.insert(20)
        bst.insert(12)
        bst.insert(25)

        #root
        assert bst.root.data == 10

        #left sub tree
        assert bst.root.left.data == 3
        assert bst.root.left.left.data == 1
        assert bst.root.left.right.data == 4

        #right sub tree
        assert bst.root.right.data == 20
        assert bst.root.right.left.data == 12
        assert bst.root.right.right.data == 25


    def test_search(self):
        bst = Bst([5,6,100,1,450,2,43, 8,3,8,7,12,])
        assert bst.search_iterative(5) == True
        assert bst.search_iterative(6) == True
        assert bst.search_iterative(100) == True
        assert bst.search_iterative(1) == True
        assert bst.search_iterative(450) == True
        assert bst.search_iterative(2) == True
        assert bst.search_iterative(43) == True
        assert bst.search_iterative(8) == True
        assert bst.search_iterative(3) == True
        assert bst.search_iterative(8) == True
        assert bst.search_iterative(7) == True
        assert bst.search_iterative(12) == True

        assert bst.search_recursive(5,bst.root) == True
        assert bst.search_recursive(6, bst.root) == True
        assert bst.search_recursive(100,bst.root) == True
        assert bst.search_recursive(1,bst.root) == True
        assert bst.search_recursive(450,bst.root) == True
        assert bst.search_recursive(2,bst.root) == True
        assert bst.search_recursive(43,bst.root) == True
        assert bst.search_recursive(8,bst.root) == True
        assert bst.search_recursive(3,bst.root) == True
        assert bst.search_recursive(8,bst.root) == True
        assert bst.search_recursive(7,bst.root) == True
        assert bst.search_recursive(12,bst.root) == True

        assert bst.search_recursive(0, bst.root) == False
        assert bst.search_recursive(23, bst.root) ==False
        assert bst.search_recursive(9, bst.root) ==False
        assert bst.search_recursive(56, bst.root) ==False
        assert bst.search_recursive(200, bst.root) == False

        assert bst.search_iterative(0) == False
        assert bst.search_iterative(23) ==False
        assert bst.search_iterative(9) ==False
        assert bst.search_iterative(56) ==False
        assert bst.search_iterative(200) == False

    def test_delete(self):
        bst = Bst([5,6,1,2,8,3])
        bst.delete(5)
        
        assert bst.search_iterative(5) == False
        assert bst.search_iterative(6) == True
        assert bst.search_iterative(1) == True
        assert bst.search_iterative(2) == True
        assert bst.search_iterative(8) == True
        assert bst.search_iterative(3) == True







    def test_get_extreme(self):
        bst = Bst([5,6,1,2,8,3])
        assert bst.get_extreme(True) == 8
        assert bst.get_extreme(False) == 1




if __name__ == '__main__':
    unittest.main()
