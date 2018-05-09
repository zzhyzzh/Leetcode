import collections
class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.window = collections.deque(maxlen=size)
        self.sum = 0
        self.size = size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.window) == self.size:
            self.sum -= self.window[0]
        self.sum += val
        self.window.append(val)

        return self.sum/float(len(self.window))

# Your MovingAverage object will be instantiated and called as such:
obj = MovingAverage(3)
param_1 = obj.next(1)
print(param_1)
param_1 = obj.next(10)
print(param_1)
param_1 = obj.next(3)
print(param_1)
param_1 = obj.next(5)
print(param_1)