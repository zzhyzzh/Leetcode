class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        single = 0
        for num in nums:
            single ^= num

        return single

solution = Solution()
result = solution.singleNumber()
print(result)
print(type(result))