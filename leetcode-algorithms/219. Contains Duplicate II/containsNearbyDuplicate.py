class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dupMap = {}
        for i, num in enumerate(nums):
            if num not in dupMap:
                dupMap[num] = i
            else:
                if i - dupMap[num] <= k:
                    return True
                else:
                    dupMap[num] = i

        return False

solution = Solution()
result = solution.containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2)
print(result)
print(type(result))