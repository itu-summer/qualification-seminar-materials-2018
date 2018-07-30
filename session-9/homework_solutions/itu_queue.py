class Queue:
    def __init__(self):
        self.items = []

    def __repr__(self):
        return str([repr(el) for el in self.items])

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def left_dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
