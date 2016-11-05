#!/usr/bin/python
# -*- coding: utf-8 -*-

class Stack(object):

    def __init__(self):
        self.items = []
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self, item):
        self.items.append(item)
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError('Pop from empty stack')
        self.size -= 1
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]
