class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        candidate = nums[0]
        sum = 0
        while i < len(nums):
            if nums[i] == candidate:
                sum += 1
            elif nums[i] != candidate:
                sum -= 1
            if sum == 0:
                candidate = nums[i + 1]
            i += 1

        if sum > 0:
            return candidate


solution = Solution()
result = solution.majorityElement([3,2,3])
print(result)