import unittest
from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):

    def test_linked_list_add(self):
        'Adiciona elemento a lista encadeada'
        le = LinkedList()
        le.add(1)

        self.assertEqual(1, len(le), 'Tamanho não é igual')

    def test_linked_list_remove_head(self):
        'Remove elemento no inicio da lista encadeada'
        le = LinkedList()
        le.add(1)  # Simula a adição do item
        le.add(2)
        le.add(3)

        item = le.remove_head()
        self.assertEqual(item, 1, 'Os elementos são diferentes')

        item = le.remove_head()
        self.assertEqual(item, 2, 'Os elementos são diferentes')

        item = le.remove_head()
        self.assertEqual(item, 3, 'Os elementos são diferentes')

        self.assertEqual(0, len(le), 'Tamanho não é igual')

    def test_linked_list_head(self):
        'Retorna o primeiro elemento da lista encadeada'
        le = LinkedList()

        le.add(1)
        le.add(2)
        le.add(3)

        item = le.head()
        self.assertEqual(item, 1, 'Os elementos são diferentes')
        self.assertEqual(3, len(le), 'Tamanho não é igual')

    def test_linked_list_tail(self):
        'Retorna o ultimo elemento da lista encadeada'
        le = LinkedList()

        le.add(1)
        le.add(2)
        le.add(3)

        item = le.tail()
        self.assertEqual(item, 3, 'Os elementos são diferentes')
        self.assertEqual(3, len(le), 'Tamanho não é igual')

    def test_linked_list_remove_tail(self):
        'Remove o ultimo elemento da lista encadeada'
        le = LinkedList()

        le.add(1)
        le.add(2)
        le.add(3)

        item = le.remove_tail()
        self.assertEqual(item, 3, 'Os elementos são diferentes')

        item = le.remove_tail()
        self.assertEqual(item, 2, 'Os elementos são diferentes')

        item = le.remove_tail()
        self.assertEqual(item, 1, 'Os elementos são diferentes')

        self.assertEqual(0, len(le), 'Tamanho não é igual')

    def test_linked_list_search(self):
        'Busca um elemento da lista encadeada'
        le = LinkedList()

        le.add(1)
        le.add(2)
        le.add(3)

        self.assertEqual(3, len(le), 'Tamanho não é igual')

        self.assertEqual(3, le.search(3), 'Os elementos são diferentes')
        self.assertEqual(1, le.search(1), 'Os elementos são diferentes')
        self.assertEqual(None, le.search(99), 'Os elementos são diferentes')


if __name__ == '__main__':
    unittest.main()
