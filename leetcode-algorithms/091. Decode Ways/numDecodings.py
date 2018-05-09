class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] != "0":
            dp = [1]
        else:
            return 0
        for i in range(1, len(s)):
            dp.append(0)
            if int(s[i]) in list(range(1, 10)):
                dp[i] = dp[i - 1]
            two_digits = int(s[i - 1:i + 1])
            if two_digits in list(range(10, 27)):
                dp[i] += dp[i - 2] if i >= 2 else 1
            elif int(s[i]) == 0:
                return 0
        return dp.pop()

solution = Solution()
result = solution.numDecodings("110")
print(result)