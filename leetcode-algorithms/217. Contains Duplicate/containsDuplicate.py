class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashSet = set()
        for num in nums:
            if num in hashSet:
                return True
            else:
                hashSet.add(num)

        return False

solution = Solution()
result = solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2])
print(result)
print(type(result))