class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split(" ")
        s = [i for i in s if i != ""]
        s = s[::-1]
        return " ".join(s)

solution = Solution()
result = solution.reverseWords(" ")
print(result)
print(type(result))