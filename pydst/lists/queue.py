#!/usr/bin/python
# -*- coding: utf-8 -*-


class Queue(object):

    def __init__(self):
        self._items = []

    def __len__(self):
        return len(self._items)

    @property
    def size(self):
        return len(self._items)

    def is_empty(self):
        return len(self._items) == 0

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop(0)
