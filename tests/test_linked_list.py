import unittest
from pydst.lists.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):

    def test_linked_list_add(self):
        'Add element in Linked List'
        le = LinkedList()
        le.add(1)

        self.assertEqual(1, len(le), 'Size doesn\'t match')

    def test_linked_list_remove_head(self):
        'Remove item from head'
        le = LinkedList()
        le.add(1)
        le.add(2)
        le.add(3)

        item = le.remove_head()
        self.assertEqual(item, 1, 'Items doesn\'t match')

        item = le.remove_head()
        self.assertEqual(item, 2, 'Items doesn\'t match')

        item = le.remove_head()
        self.assertEqual(item, 3, 'Items doesn\'t match')

        self.assertEqual(0, len(le), 'Size doesn\'t match')

    def test_linked_list_head(self):
        'Return head item from Linked List'
        le = LinkedList()

        le.add(1)
        le.add(2)
        le.add(3)

        item = le.head()
        self.assertEqual(item, 1, 'Items doesn\'t match')
        self.assertEqual(3, len(le), 'Size doesn\'t match')

    def test_linked_list_tail(self):
        'Return tail item from Linked List'
        le = LinkedList()

        le.add(1)
        le.add(2)
        le.add(3)

        item = le.tail()
        self.assertEqual(item, 3, 'Items doesn\'t match')
        self.assertEqual(3, len(le), 'Size doesn\'t match')

    def test_linked_list_remove_tail(self):
        'Remove tail item from Linked List'
        le = LinkedList()

        le.add(1)
        le.add(2)
        le.add(3)

        item = le.remove_tail()
        self.assertEqual(item, 3, 'Items doesn\'t match')

        item = le.remove_tail()
        self.assertEqual(item, 2, 'Items doesn\'t match')

        item = le.remove_tail()
        self.assertEqual(item, 1, 'Items doesn\'t match')

        self.assertEqual(0, len(le), 'Size doesn\'t match')

    def test_linked_list_search(self):
        'Search item in Linked List'
        le = LinkedList()

        le.add(1)
        le.add(2)
        le.add(3)


        self.assertEqual(3, len(le), 'Size doesn\'t match')

        self.assertEqual(3, le.search(3), 'Items doesn\'t match')
        self.assertEqual(1, le.search(1), 'Items doesn\'t match')
        self.assertEqual(None, le.search(99), 'Items doesn\'t match')


if __name__ == '__main__':
    unittest.main()
