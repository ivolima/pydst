#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Ivo Romario <ivo.romario@gmail.com>
# License:

import unittest

from pydst.trees.node import Node
from pydst.trees.binary_search_tree import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):

    def setUp(self):
        # creating an empty tree
        self.bst = BinarySearchTree()

    def add_fake_elements(self):
        self.bst.add(3)
        self.bst.add(2)
        self.bst.add(1)
        self.bst.add(4)
        self.bst.add(5)

    def test_empty_tree(self):
        """
        Test if tree is empty
        """
        self.assertTrue(self.bst.is_empty(), 'Tree should be empty')
        self.bst.add(5)
        self.assertFalse(self.bst.is_empty(), 'Tree shouldn\'t be empty')

    def test_add_node(self):
        """
        Adding a single node
        """
        self.bst.add(42)
        self.assertIsInstance(self.bst.root, Node, 'Obj type doesn\'t match')
        self.assertEqual(42, self.bst.root.value, 'Root value doesn\'t match')
        self.assertEqual(1, len(self.bst), 'Tree size doesn\'t match')

    def test_add_left_node(self):
        """
        Adding a left node
        """
        self.bst.add(15)
        self.bst.add(10)
        self.assertEqual(2, len(self.bst), 'Tree size doesn\'t match')
        self.assertIsInstance(self.bst.root.left, Node, 'Obj type doesn\'t match')
        left_node = self.bst.get_left(self.bst.root)
        self.assertEqual(10, left_node.value, 'Node value doesn\'t match')

    def test_add_right_node(self):
        """
        Adding a right node
        """
        self.bst.add(15)
        self.bst.add(50)
        self.assertEqual(2, len(self.bst), 'Tree size doesn\'t match')
        self.assertIsInstance(self.bst.root.right, Node, 'Obj doesn\'t match')
        right_node = self.bst.get_right(self.bst.root)
        self.assertEqual(50, right_node.value, 'Node value doesn\'t match')

    def test_add_duplicated_value(self):
        """
        Adding the same value twice
        """
        self.bst.add(42)
        self.bst.add(42)
        self.assertEqual(1, len(self.bst), 'Repeated values should be ignored')

    def test_traversal_invalid_method(self):
        """
        Traversins tree using an invalid method
        """
        with self.assertRaises(ValueError):
            self.bst.traversal(method='invalid')

    def test_traversal_inorder(self):
        """
        Traversing tree using inorder method
        """
        self.add_fake_elements()
        result = self.bst.traversal(method='inorder')
        self.assertIsInstance(result, list, 'Return must be a list instance')
        self.assertListEqual([1, 2, 3, 4, 5], result,'Result doesn\'t match')

    def test_traversal_preorder(self):
        """
        Traversing tree using preorder method
        """
        self.add_fake_elements()
        result = self.bst.traversal(method='preorder')
        self.assertIsInstance(result, list, 'Return must be a list instance')
        self.assertListEqual([3, 2, 1, 4, 5], result,'Result doesn\'t match')

    def test_traversal_postorder(self):
        """
        Traversing tree using postorder method
        """
        self.add_fake_elements()
        result = self.bst.traversal(method='postorder')
        self.assertIsInstance(result, list, 'Return must be a list instance')
        self.assertListEqual([1, 2, 5, 4, 3], result,'Result doesn\'t match')

    def test_traversal_empty_tree(self):
        """
        Traversing an empty tree
        """
        methods = ['inorder', 'preorder', 'postorder']
        for method in methods:
            result = self.bst.traversal(method=method)
            self.assertIsInstance(result, list, 'Return must be a list instance')
            self.assertListEqual([], result,'Result should be empty list')

    def test_search_empty_tree(self):
        """
        Searching a node in an empty tree
        """
        node = self.bst.search(15)
        self.assertIsNone(node, 'Return must be None because tree is empty')

    def test_search_inexistent_value(self):
        """
        Searching a node that doesn't exist in tree
        """
        self.add_fake_elements()
        node = self.bst.search(15)
        self.assertIsNone(node, 'Return must be None because node isn\'t in tree')

    def test_search_existent_value(self):
        """
        Searching existent nodes at different positions in tree
        """
        self.add_fake_elements()
        root_node = self.bst.search(3)
        intermediate_node = self.bst.search(2)
        leaf_node = self.bst.search(1)
        self.assertIsNone(root_node.parent, 'Node should\'t have parent')
        self.assertTrue(leaf_node.is_leaf(), 'Node should be a leaf')
        self.assertEqual(3, root_node.value, 'Node value doesn\'t match')
        self.assertEqual(2, intermediate_node.value, 'Node value doesn\'t match')
        self.assertEqual(1, leaf_node.value, 'Node value doesn\'t match')

    def test_extremes(self):
        self.assertTrue(False, 'Continue tests from here')

if __name__ == '__main__':
    unittest.main()
