class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        bucket, index = self._index(key)
        array = self.buckets[bucket]
        if index < 0:
            array.append((key, value))
        else:
            array[index] = (key, value)

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        bucket, index = self._index(key)
        if index < 0:
            return -1
        array = self.buckets[bucket]
        key, value = array[index]
        return value

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        bucket, index = self._index(key)
        if index < 0:
            return
        array = self.buckets[bucket]
        del array[index]

    def _bucket(self, key):
        return key % self.size

    def _index(self, key):
        bucket = self._bucket(key)
        for i, (k, v) in enumerate(self.buckets[bucket]):
            if k == key:
                return bucket, i
        return bucket, -1

hashMap = MyHashMap()
hashMap.put(1, 1)
hashMap.put(2, 2)
hashMap.get(1)      #            // returns 1
hashMap.get(3)      #            // returns -1 (not found)
hashMap.put(2, 1)   #          // update the existing value
hashMap.get(2)      #            // returns 1
hashMap.remove(2)   #          // remove the mapping for 2
hashMap.get(2)      #