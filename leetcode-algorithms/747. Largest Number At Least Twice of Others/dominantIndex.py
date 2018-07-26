class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxNum = max(nums)
        for i in range(len(nums)):
            if nums[i] == maxNum:
                maxIndex = i
                continue
            if nums[i] * 2 > maxNum:
                return -1
        return maxIndex


solution = Solution()
result = solution.dominantIndex([3, 6, 1, 0])
print(result)
print(type(result))