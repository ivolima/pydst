#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Ivo Romario <ivo.romario@gmail.com>
# License:

from node import Node


class BinarySearchTree(object):

    __TRAVERSAL_METHODS = ['inorder', 'preorder', 'postorder']

    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.root == None

    def get_left(self, node):
        return node.left

    def get_right(self, node):
        return node.right

    def add(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
        else:
            # search for a place to insert, starting from root node
            parent = self.root
            while parent.value != value:
                if value < parent.value:
                    if parent.left is None:
                        break
                    parent = parent.left
                elif value > parent.value:
                    if parent.right is None:
                        break
                    parent = parent.right
                else:
                    return

            if value == parent.value:
                return

            new_node.parent = parent

            if value < parent.value:
                parent.left = new_node
            else:
                parent.right = new_node
        self.size += 1

    def _inorder(self, node, elements=[]):
        if node is None:
            return

        self._inorder(node.left, elements)
        elements.append(node.value)
        self._inorder(node.right, elements)

        return elements

    def _preorder(self, node, elements=[]):
        elements.append(node.value)
        if node.left is not None:
            self._preorder(node.left, elements)
        if node.right is not None:
            self._preorder(node.right, elements)

        return elements

    def _postorder(self, node, elements=[]):
        if node.left is not None:
            self._postorder(node.left, elements)
        if node.right is not None:
            self._postorder(node.right, elements)
        elements.append(node.value)
        return elements

    def traversal(self, method='inorder'):
        """
        Traverse tree using a pre-selected method

        Parameters:
        method:
        Example:
        self.bst = BinarySearchTree()
        self.bst.add(1)
        self.bst.add(2)
        self.bst.add(3)
        self.bst.add(4)
        self.bst.add(5)

        print "Inorder traversal of binary tree is"
        print self.bst.traversal(method='inorder')
        1 2 4 5 3

        print "Preorder traversal of binary tree is"
        print self.bst.traversal(method='preorder')
        3 2 1 4 5
        print "Postorder traversal of binary tree is"
        print self.bst.traversal(method='postorder')
        4 5 2 3 1

        """
        if method not in self.__TRAVERSAL_METHODS:
            raise ValueError

        if self.root is None:
            return []
        if method == 'inorder':
            return self._inorder(self.root)
        elif method == 'preorder':
            return self._preorder(self.root)
        else:
            return self._postorder(self.root)
