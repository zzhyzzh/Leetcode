class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hastTable = []

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        if key not in self.hastTable:
            self.hastTable.append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        if key in self.hastTable:
            self.hastTable.remove(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        if key in self.hastTable:
            return True
        else:
            return False


hashSet = MyHashSet()
hashSet.add(1)
hashSet.add(2)
hashSet.contains(1)     # returns true
hashSet.contains(3)     #    // returns false (not found)
hashSet.add(2)
hashSet.contains(2)     #    // returns true
hashSet.remove(2)
hashSet.contains(2)     #    // returns false (already removed)
