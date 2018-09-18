class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap = {}
        for i, num in enumerate(nums):
            if target - num in hashMap:
                return [hashMap[target - num], i]
            else:
                hashMap[num] = i

solution = Solution()
result = solution.twoSum([3, 2, 4], 6)
print(result)
