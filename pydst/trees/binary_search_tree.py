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
        return self.root is None

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

    def search(self, value, start=None):
        node = start if start is not None else self.root

        if self.is_empty():
            return None

        if value == node.value:
            return node
        elif value < node.value and node.left is not None:
            return self.search(value, node.left)
        elif value > node.value and node.right is not None:
            return self.search(value, node.right)
        else:
            return None

    def _extremes(self, node, find_min=True):
        if self.is_empty():
            return None

        keep_left = (find_min and node.left is not None)
        keep_right = (not find_min and node.right is not None)

        while keep_left or keep_right:
            if find_min and node.left is not None:
                node = node.left
            elif not find_min and node.right is not None:
                node = node.right
            else:
                break
        return node

    def get_min(self, node=None):
        node = node if node else self.root
        return self._extremes(node, find_min=True)

    def get_max(self, node=None):
        node = node if node else self.root
        return self._extremes(node, find_min=False)

    def has_left(self, node):
        return node.left is not None

    def has_right(self, node):
        return node.right is not None

    def _remove_leaf(self, node):
        parent = node.parent
        if parent is not None:
            if parent.left == node:
                parent.left = None
            else:
                parent.right = None
        node.parent = None
        return node

    def _pass_child_up(self, node):
        parent = node.parent
        child = node.left if node.left is not None else node.right
        child.parent = parent

        if parent.left == node:
            parent.left = child
        else:
            parent.right = child

        return node

    def depth(self, node):
        if node is None:
            return 0
        return 1  + max(self.depth(node.left) if node.left is not None else 0,
                        self.depth(node.right) if node.right is not None else 0)

    def _successor(self, node):
        # checks which side has biggest subtree
        if self.depth(node.left) < self.depth(node.right):
            return self.get_min(node.right)
        return self.get_max(node.left)

    def remove(self, value):
        node = self.search(value)
        if node is None:
            return None
        if node.is_leaf():
            # just remove it
            self.size -= 1
            return self._remove_leaf(node)
        elif node.left is not None and node.right is not None:
            # both children are present; find sucessor
            successor = self._successor(node)
            if not successor.is_leaf():
                self._pass_child_up(successor)
            node.value = successor.value
            self.size -= 1
            return Node(node.value)
        else:
            # only one child is present
            self.size -= 1
            return self._pass_child_up(node)

    def _inorder(self, node, elements=None):
        if node is None:
            return

        elements = [] if elements is None else elements
        self._inorder(node.left, elements)
        elements.append(node.value)
        self._inorder(node.right, elements)

        return elements

    def _preorder(self, node, elements=None):
        elements = [] if elements is None else elements
        elements.append(node.value)

        if node.left is not None:
            self._preorder(node.left, elements)
        if node.right is not None:
            self._preorder(node.right, elements)

        return elements

    def _postorder(self, node, elements=None):
        elements = [] if elements is None else elements

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
