class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        palin_1 = self.singleType(s);
        palin_2 = self.doubleType(s);

        return palin_1 if len(palin_1) > len(palin_2) else palin_2

    def singleType(self, s):
        palin = s[0]
        for i in range(len(s)):
            palin_len = 1
            while i - palin_len >= 0 and i + palin_len < len(s):
                if s[i - palin_len] == s[i + palin_len]:
                    palin_len += 1
                else:
                    break
            temp = s[i - (palin_len - 1) : i + (palin_len - 1) + 1]
            if len(temp) > len(palin):
                palin = temp

        return palin

    def doubleType(self, s):
        palin = s[0]
        for i in range(1, len(s)):
            palin_len = 1
            while i - palin_len >= 0 and i + palin_len - 1 < len(s):
                if s[i - palin_len] == s[i + palin_len - 1]:
                    palin_len += 1
                else:
                    break
            temp = s[i - (palin_len - 1): i + (palin_len - 1)]
            if len(temp) > len(palin):
                palin = temp

        return palin

solution = Solution()
result = solution.longestPalindrome("babad")
print(result)
print(type(result))
