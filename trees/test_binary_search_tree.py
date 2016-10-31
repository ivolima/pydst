#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Ivo Romario <ivo.romario@gmail.com>
# License:

import unittest

from node import Node
from binary_search_tree import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):

    def test_binary_search_tree_add(self):
        # creating an empty tree
        bst = BinarySearchTree()
        self.assertIsNone(bst.root, 'Tree root should be empty')

        # added a single node
        bst.add(42)
        self.assertIsInstance(bst.root, Node, 'Obj type doesn\'t match')
        self.assertEqual(42, bst.root.value, 'Root value doesn\'t match')
        self.assertEqual(1, len(bst), 'Tree size doesn\'t match')

        # added a node to the left
        bst.add(10)
        self.assertEqual(2, len(bst), 'Tree size doesn\'t match')
        self.assertIsInstance(bst.root.left, Node, 'Obj type doesn\'t match')
        self.assertEqual(10, bst.root.left.value, 'Node value doesn\'t match')

        # added a node to the right
        bst.add(50)
        self.assertEqual(3, len(bst), 'Tree size doesn\'t match')
        self.assertIsInstance(bst.root.right, Node, 'Obj doesn\'t match')
        self.assertEqual(50, bst.root.right.value, 'Node value doesn\'t match')

        # added a node with repeated value
        bst.add(42)
        self.assertEqual(3, len(bst), 'Repeated values should be ignored')


if __name__ == '__main__':
    unittest.main()
