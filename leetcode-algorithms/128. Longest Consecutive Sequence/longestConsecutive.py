class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLength = 0
        nums = set(nums)
        for num in nums:
            if num - 1 not in nums:
                currNum = num
                currLength = 1
                while currNum + 1 in nums:
                    currNum += 1
                    currLength += 1
                maxLength = max(maxLength, currLength)

        return maxLength

