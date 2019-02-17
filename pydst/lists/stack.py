class Stack:

	def __init__(self):
		self._items = []

	def __len__(self):
		return len(self._items)

	def is_empty(self):
		return len(self._items) == 0

	def push(self, data):
		self._items.append(data)

	def pop(self):
		if self.is_empty():
			raise IndexError("It is impossible pop empty stack")
		return self._items.pop()

	def peek(self):
		return self._items[len(self._items)-1]
