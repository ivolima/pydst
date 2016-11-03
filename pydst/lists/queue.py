#!/usr/bin/python
# -*- coding: utf-8 -*-

class Queue(object):

    def __init__(self):
        self.items = []
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def enqueue(self, item):
        self.items.insert(0, item)
        self.size += 1

    def dequeue(self):
        self.items.pop(0)
        self.size -= 1

