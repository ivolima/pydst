class Node(object):
    def __init__(self, value):
        self.parent = None
        self.left = None
        self.right = None
        self.value = value

    def is_leaf(self):
        return self.left is None and self.right is None


class BinarySearchTree(object):

    _TRANSVERSAL_METHODS  = ['inorder', 'preorder', 'postorder' ]

    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.root is None

    def get_left(self, node):
        return node.left

    def get_right(self, node):
        return node.right

    def add(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
        else:
            parent = self.root
            while parent.value != value:
                if value < parent.value:
                    if parent.left is None:
                        break
                    parent = parent.left

                elif value > parent.value:
                    if parent.right is None:
                        break
                    parent = parent.right
                else:
                    return

            if value == parent.value:
                return

            new_node.parent = parent

            if value < parent.value:
                parent.left = new_node
            else:
                parent.right = new_node
        self.size += 1

    def search(self, value, start=None):
        node = start if start is not None else self.root
        if self.is_empty():
            return None

        if value == node.value:
            return node
        elif value < node.value and node.left is not None:
            return self.search(value, node.left)
        elif value > node.value and node.right is not None:
            return self.search(value, node.right)
        else:
            return None


    def _extremes(self, node, find_min=True):
        if self.is_empty():
            return None
        keep_left = (find_min and node.left is not None)
        keep_right = (not find_min and node.right is not None)

        while keep_left or keep_right:
            if find_min and node.left is not None:
                node = node.left
            elif not find_min and node.right is not None:
                node = node.right
            else:
                break
        return node

    def get_min(self, node=None):
        node = node if node else self.root
        return self._extremes(node, find_min=True)

    def get_max(self, node=None):
        node = node if node else self.root
        return self._extremes(node, find_min=False)

    def has_left(self, node):
        return node.left is not None

    def has_right(self, node):
        return node.right is not None

    def _remove_leaf(self, node):
        parent = node.parent
        if parent is not None:
            if parent.left == node:
                parent.left = None
            else:
                parent.right = None
        node.parent = None
        return node

    def _pass_child_up(self, node):
        parent = node.parent 
        child = node.left if node.left is not None else node.right
        child.parent = parent

        if parent.left == node:
            parent.left = child 
        else:
            paren.right = child
        return node

    def depth(self, node):
        if node is None:
            return 0
        return 1 + max(self.depth(node.left) if node.left is not None else 0,
                       self.depth(node.right) if node.right is not None else 0)

    def _successor(self, node):
        if self.depth(node.left) < self.depth(node.right):
            return self.get_min(node.right)
        return self.get_min(node.left)

    def remove(self, value):
        node = self.search(value)
        if node is None:
            return None
        
        if node.is_leaf():
            self.size -= 1
            return self._remove_leaf(node)
        elif node.left is not None and node.right is not None:
            successor = self._successor(node)
            if not successor.is_leaf():
                self._pass_child_up(successor)
            node.value = successor.value
            self.size -= 1
            return Node(node.value)
        else:
            self.size -= 1
            return self._pass_child_up(node)

    def _inorder(self, node, elements=None):
        if node is None:
            return

        elements = [] if elements is None else elements
        self._inorder(node.left, elements)
        elements.append(node.value)
        self._inorder(node.right, elements)
        return elements

    def _preorder(self, node, elements=None):
        elements = [] if elements is None else elements
        elements.append(node.value)

        if node.left is not None:
            self._preorder(node.left, elements)

        if node.right is not None:
            self._preorder(node.right, elements)

        return elements


    def _postorder(self, node, elements=None):
        elements = [] if elements is None else elements

        if node.left is not None:
            self._postorder(node.left, elements)
        if node.right is not None:
            self._postorder(node.right, elements)

        elements.append(node.value)
        return elements


    def traversal(self, method='inorder'):
        if method not in self._TRANSVERSAL_METHODS:
            raise ValueError

        if self.root is None:
            return []
        if method == 'inorder':
            return self._inorder(self.root)
        elif method == 'preorder':
            return self._preorder(self.root)
        else:
            return self._postorder(self.root)

