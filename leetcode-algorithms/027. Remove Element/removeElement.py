class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        k = len(nums) - 1
        if nums == []:
            return i
        while i <= k:
            if nums[i] == val:
                nums[i], nums[k] = nums[k], nums[i]
                k -= 1
                continue
            i += 1

        return i


solution = Solution()
result = solution.removeElement(nums = [1], val = 1)
print(result)
print(type(result))