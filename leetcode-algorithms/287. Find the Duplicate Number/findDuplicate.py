class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fastPtr = 0
        slowPtr = 0
        while True:
            fastPtr = nums[fastPtr]
            fastPtr = nums[fastPtr]
            slowPtr = nums[slowPtr]
            if fastPtr == slowPtr:
                break
        Ptr = 0
        while True:
            Ptr = nums[Ptr]
            slowPtr = nums[slowPtr]
            if Ptr == slowPtr:
                return Ptr