class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return True if n % 4 != 0 else False

solution = Solution()
result = solution.hasAlternatingBits(5)
print(result)
print(type(result))