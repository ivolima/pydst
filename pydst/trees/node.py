#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Ivo Romario <ivo.romario@gmail.com>
# License:

class Node(object):

    def __init__(self, value):
        self.parent = None
        self.left = None
        self.right = None
        self.value = value

    def is_leaf(self):
        return self.left is None and self.right is None
