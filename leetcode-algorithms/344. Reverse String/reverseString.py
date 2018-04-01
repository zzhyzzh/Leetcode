class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """

        return s[::-1]

solution = Solution()
result = solution.reverseString("hello")
print(result)
print(type(result))
