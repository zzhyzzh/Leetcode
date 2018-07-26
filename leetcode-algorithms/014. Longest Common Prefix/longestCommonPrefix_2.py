class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        LCP = ""
        maxLen = 0
        if strs == [] or strs[0] == "":
            return LCP
        else:
            j = 0
            LCP_temp = strs[0][0 : j]
        while True:
            for i in range(1, len(strs)):
                if strs[i][0:len(LCP_temp)] != LCP_temp:
                    return LCP
            if j == len(strs[0]):
                return strs[0][0 : j + 1]
            j += 1
            LCP = LCP_temp
            LCP_temp = strs[0][0 : j]


solution = Solution()
result = solution.longestCommonPrefix(["aa","aa"])
print(result)
print(type(result))