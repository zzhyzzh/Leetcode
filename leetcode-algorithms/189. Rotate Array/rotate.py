class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[:] = nums[n - k:] + nums[:n - k]


solution = Solution()
result = solution.rotate([1,2,3,4,5,6,7], 3)
print(result)
print(type(result))