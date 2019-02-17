import unittest
import sys

from pydst.sorts.sort import Sort


class TestSort(unittest.TestCase):
    def setUp(self):
        self.le = Sort()

    def test_bouble_add(self):
        'Add element in a Bouble'
        self.le.add(10)
        self.le.add(7)
        self.le.add(5)
        self.le.add(6)
        self.le.add(3)

        self.assertEqual(5, len(self.le), 'Size doesn\'t match')

    def test_bouble_remove(self):
        'Remove item from a bouble'
        self.le.add(1)
        self.le.add(2)
        self.le.add(3)

        item = self.le.remove()
        self.assertEqual(item, 1, 'Items doesn\'t match')

        item = self.le.remove()
        self.assertEqual(item, 2, 'Items doesn\'t match')

        item = self.le.remove()
        self.assertEqual(item, 3, 'Items doesn\'t match')

        self.assertEqual(0, len(self.le), 'Size doesn\'t match')

    def test_bouble_sort(self):
        'Sort a list of elements'
        self.le.add(10)
        self.le.add(7)
        self.le.add(5)
        self.le.add(6)
        self.le.add(3)

        sorted_list = self.le.bouble_sort()
        self.assertEqual([3,5,6,7,10], sorted_list, 'Size doesn\'t match')

    def test_merge_sort(self):
        'Merge and sort list'
        unsorted_list = [83, 94, 35, 2, 10, 8, 70]
        for idx in unsorted_list:
            self.le.add(idx)

        sorted_list = self.le.merge_sort()

        self.assertEqual([2, 8, 10, 35, 70, 83, 94], sorted_list, 'Size doesn\'t match')

    def test_insertation_sort(self):
        'Insertation sort'
        #unsorted_list = [19,7,31,45,30,11,121, 2]
        unsorted_list = [2,5,3,18,10,27,1]
        for idx in unsorted_list:
            self.le.add(idx)
        sorted_list = self.le.insertion_sort()
        self.assertEqual([1,2,3,5,10,18,27], sorted_list, 'Size doesn\'t match')

    def test_selection_sort(self):
        'Selection sort'
        unsorted_list = [20,45,23,1,2,4,9,3,90,5]
        for idx in unsorted_list:
            self.le.add(idx)
        sorted_list = self.le.selection_sort()
        self.assertEqual([1,2,3,4,5,9,20,23,45,90], sorted_list, 'Size doesn\'t match')


    def test_heap_sort(self):
        'Heap sort'
        unsorted_list = [20,45,23,1,2,4,9,3,90,5]
        for idx in unsorted_list:
            self.le.add(idx)
        sorted_list = self.le.heap_sort()
        self.assertEqual([1,2,3,4,5,9,20,23,45,90], sorted_list, 'Size doesn\'t match')

#    def test_linked_list_tail(self):
#        'Return tail item from Linked List'
#        le = LinkedList()
#
#        le.add(1)
#        le.add(2)
#        le.add(3)
#
#        item = le.tail()
#        self.assertEqual(item, 3, 'Items doesn\'t match')
#        self.assertEqual(3, len(le), 'Size doesn\'t match')
#
#    def test_linked_list_remove_tail(self):
#        'Remove tail item from Linked List'
#        le = LinkedList()
#
#        le.add(1)
#        le.add(2)
#        le.add(3)
#
#        item = le.remove_tail()
#        self.assertEqual(item, 3, 'Items doesn\'t match')
#
#        item = le.remove_tail()
#        self.assertEqual(item, 2, 'Items doesn\'t match')
#
#        item = le.remove_tail()
#        self.assertEqual(item, 1, 'Items doesn\'t match')
#
#        self.assertEqual(0, len(le), 'Size doesn\'t match')
#
#    def test_linked_list_search(self):
#        'Search item in Linked List'
#        le = LinkedList()
#
#        le.add(1)
#        le.add(2)
#        le.add(3)
#
#        print(le.search(3))
#
#        self.assertEqual(3, len(le), 'Size doesn\'t match')
#
#        self.assertEqual(3, le.search(3), 'Items doesn\'t match')
#        self.assertEqual(1, le.search(1), 'Items doesn\'t match')
#        self.assertEqual(None, le.search(99), 'Items doesn\'t match')
#

if __name__ == '__main__':
    unittest.main()
