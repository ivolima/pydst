#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Ivo Romario <ivo.romario@gmail.com>
# License:

import unittest
from pydst.lists.stack import Stack


class TestStack(unittest.TestCase):

    def setUp(self):
        # creating an empty stack
        self.s = Stack()

    def test_is_empty(self):
        """Checking if stack is empty"""
        self.assertTrue(self.s.is_empty(), 'Stack should be empty')

    def test_push(self):
        """Pushing elements to the stack"""
        self.s.push(1)
        self.s.push(5)
        self.assertEqual(2, len(self.s), 'Stack should have two elements')

    def test_pop(self):
        """Popping element from a stack"""
        self.assertRaises(IndexError, self.s.pop)
        self.s.push(1)
        item = self.s.pop()
        self.assertEqual(1, item, 'Item doesn\'t match')

    def test_peek(self):
        """Getting top element of the stack"""
        self.assertRaises(IndexError, self.s.peek)
        self.s.push(3)
        self.s.push(5)
        item = self.s.peek()
        self.assertEqual(5, item, 'Peek element doesn\'t match')

