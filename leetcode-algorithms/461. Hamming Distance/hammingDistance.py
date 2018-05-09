class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        count = 0
        temp = x ^ y
        while temp:
            count += temp & 1
            temp = temp >> 1

        return count

solution = Solution()
result = solution.hammingDistance(1, 4)
print(result)
print(type(result))