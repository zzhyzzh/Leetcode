import random

class Solution(object):
    nums = []
    origin = []
    length = 0
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.origin = list(nums)
        self.length = len(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.origin

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        for i in range(self.length):
            index = random.randrange(i, self.length)
            self.nums[i], self.nums[index] = self.nums[index], self.nums[i]

        return self.nums


# Your Solution object will be instantiated and called as such:
nums = [1,2,3]
obj = Solution(nums)
param_2 = obj.shuffle()
print(param_2)
param_1 = obj.reset()
print(param_1)
param_2 = obj.shuffle()
print(param_2)