class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """

        return a if b == 0 else self.getSum(a ^ b, (a & b) << 1)

solution = Solution()
result = solution.getSum(1, -1)
print(result)