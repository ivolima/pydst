#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Ivo Romario <ivo.romario@gmail.com>
# License:

import unittest
from pydst.lists.heap import Heap


class TestHeap(unittest.TestCase):

    def setUp(self):
        # creating an empty heap
        self.q = Heap()

    def test_push(self):
        """Adding element to heap"""
        import ipdb; ipdb.set_trace()
        self.q.push(4)
        self.q.push(8)
        self.q.push(10)
        self.assertEqual(3, len(self.q), 'Size doesn\'t match')

