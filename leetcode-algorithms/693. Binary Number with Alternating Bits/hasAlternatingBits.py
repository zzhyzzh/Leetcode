class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        flag = n & 1
        n = n >> 1
        while n:
            if flag == n & 1:
                return False
            flag = n & 1
            n = n >> 1
        return True

solution = Solution()
result = solution.hasAlternatingBits(5)
print(result)
print(type(result))