class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """

        def toStr(l, u):
            if l == u:
                return str(l)
            else:
                return str(l) + "->" + str(u)

        ranges = []
        i, j = lower, 0
        while i < upper + 1:
            if j == len(nums):
                ranges.append(toStr(i, upper))
                break
            if i < nums[j]:
                ranges.append(toStr(i, nums[j] - 1))
                i = nums[j] + 1
                j += 1
            elif i == nums[j]:
                i += 1
                j += 1
            elif i > nums[j]:
                j += 1
        return ranges



