class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        i, j = 0, len(s) - 1
        r = list(s)
        while i < j:
            r[i], r[j] = r[j], r[i]
            i += 1
            j -= 1
        return "".join(r)

solution = Solution()
result = solution.reverseString("hello")
print(result)
print(type(result))
