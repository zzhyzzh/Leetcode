class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        nums.sort()
        for i in range(0, len(nums), 2):
            sum += nums[i]

        return sum

solution = Solution()
result = solution.arrayPairSum([1,4,3,2])
print(result)
print(type(result))