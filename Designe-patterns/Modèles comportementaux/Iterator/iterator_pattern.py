from collections.abc import Iterator, Iterable

# Custom Iterator
class NameIterator(Iterator):
    def __init__(self, names):
        self._names = names
        self._index = 0

    def __next__(self):
        if self._index < len(self._names):
            name = self._names[self._index]
            self._index += 1
            return name
        raise StopIteration

# Custom Iterable
class NameCollection(Iterable):
    def __init__(self, names):
        self._names = names

    def __iter__(self):
        return NameIterator(self._names)

# Client Code
names = NameCollection(["Alice", "Bob", "Charlie", "David"])
for name in names:
    print(name)
