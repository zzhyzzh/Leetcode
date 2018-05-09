class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        candyType = len(set(candies))
        return min(candyType, len(candies)/2)

solution = Solution()
result = solution.distributeCandies([1,1,2,2,3,3])
print(result)
print(type(result))