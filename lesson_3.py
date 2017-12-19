import sys

class HashTable:
    _length = 8
    _objects = []

    def __init__(self, length=None):
        if isinstance(length, int):
            self._length = length
        self._objects = [None] * self._length

    def hash(self, val):
        charSum = 0
        for c in val:
            charSum += ord(c)
        return charSum % len(self._objects)

    def add(self, val):
        self.__resizeIfNeeded()
        h = self.hash(val)
        if self._objects[h] is None:
            #print("insert {0} to position {1}".format(val, h))
            self._objects[h] = val
            return True
        #print("insert {0} to position {1} failed. There is already {2}".format(val, h, self._objects[h]))
        return False

    def rem(self, val):
        self.__resizeIfNeeded()
        h = self.hash(val)
        if self._objects[h] is not None:
            #print("delete {0} from position {1}".format(val, h))
            self._objects[h] = None
            return True
        return False

    def __resizeIfNeeded(self):
        shouldResize = self._objects.count(None) / len(self._objects) < 0.25
        if not shouldResize:
            return False
        tempObjects = [None] * (len(self._objects) + self._length)
        for obj in self._objects:
            if obj is None:
                continue
            h = self.hash(obj)
            if tempObjects[h] is None:
                tempObjects[h] = obj
        #print("resize needed. old: {0} new: {1}".format(self._objects, tempObjects))
        self._objects = tempObjects
        return True

    def find(self, val):
        h = self.hash(val)
        if self._objects[h] is None:
            return None
        return h

    def exists(self, val):
        i = self.find(val)
        if i is None:
            return False
        return True

#if __name__ == '__main__':
rows = [line.strip() for line in sys.stdin]
hashTable = HashTable()
ops = {
    '+': hashTable.add,
    '-': hashTable.rem,
    '?': hashTable.exists,
}
res = {
    True: 'OK',
    False: 'FAIL'
}
for inputValue in rows:
    op = ops[inputValue[:1]]
    opResult = op(inputValue[2:])
    print(res[opResult])
