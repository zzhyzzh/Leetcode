class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        small = 0
        big = len(numbers) - 1
        while big > small:
            if numbers[small] + numbers[big] > target:
                big -= 1
            elif numbers[small] + numbers[big] < target:
                small += 1
            elif numbers[small] + numbers[big] == target:
                return [small + 1, big + 1]

solution = Solution()
result = solution.twoSum(numbers = [2,7,11,15], target = 9)
print(result)
print(type(result))