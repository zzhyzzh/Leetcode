class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Sum = sum(nums)
        left = 0
        for i in range(len(nums)):
            if Sum - left - nums[i] == left:
                return i
            else:
                left += nums[i]

        return -1


solution = Solution()
result = solution.pivotIndex([1, 7, 3, 6, 5, 6])
print(result)
print(type(result))