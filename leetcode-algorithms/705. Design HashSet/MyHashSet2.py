class MyHashSet:

    def __init__(self):
        self.arr = [False] * 1000000

    def add(self, key):
        self.arr[key] = True

    def remove(self, key):
        self.arr[key] = False

    def contains(self, key):
        return self.arr[key]


hashSet = MyHashSet()
hashSet.add(1)
hashSet.add(2)
hashSet.contains(1)     # returns true
hashSet.contains(3)     #    // returns false (not found)
hashSet.add(2)
hashSet.contains(2)     #    // returns true
hashSet.remove(2)
hashSet.contains(2)     #    // returns false (already removed)
