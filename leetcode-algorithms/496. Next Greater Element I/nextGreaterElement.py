class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        map = {}
        if nums:
            stack = [nums[0]]
        else:
            return []
        NGE = []
        i = 1
        while i < len(nums):
            while stack and nums[i] > stack[-1]:
                map[stack.pop()] = nums[i]
            stack.append(nums[i])
            i += 1
        for left in stack:
            map[left] = -1
        for num in findNums:
            NGE.append(map[num])

        return NGE

solution = Solution()
result = solution.nextGreaterElement([4,1,2], [1,3,4,2])
print(result)
print(type(result))