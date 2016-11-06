#!/usr/bin/python
# -*- coding: utf-8 -*-

class Heap(object):

    def __init__(self, heap_min=True):
        self.heap = []
        self.size = 0
        self.HEAP_MIN = heap_min

    def __len__(self):
        return self.size

    def __str__(self):
        tree = ''
        for i in xrange(self.size):
            node = self.heap[i]
            l = self._left(i)
            r = self._right(i)
            left = self.heap[l] if l < self.size else '-'
            right = self.heap[r] if r < self.size else '-'
            tree += 'Node: {}, Left: {}, Right: {}\n'.format(node, left, right)
        return tree

    def is_empty(self):
        return self.size == 0

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _parent(self, i):
        return -1 if i == 0 else (i - 1) / 2

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2

    def _heapify(self, i):
        largest = i
        l = self._left(i)
        r = self._right(i)

        if l <= self.size and self.heap[l] > self.heap[i]:
            largest = l
        if r <= self.size and self.heap[r] > self.heap[largest]:
            largest = r
        if largest != i:
            # exchange self.heap[i] with self.heap[largest]
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self._heapify(largest)

    def peek(self):
        if self.is_empty():
            return None
        return self.heap[0]

    def push(self, item):
        i = self.size
        self.heap.append(item)
        p = self._parent(i)

        while p != -1 and self.heap[i] < self.heap[p]:
            self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
            i = p
            p = self._parent(i)

        self.size += 1

    def pop(self):
        if self.is_empty():
            return
        _root = self.peek()
        self._swap(0, -1)
        self.heap.pop()
        self.size -= 1
        self._heapify(0)
        return _root

