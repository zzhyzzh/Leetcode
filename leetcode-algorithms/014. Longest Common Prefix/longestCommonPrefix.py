import re

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        LCP = ""
        maxLen = 0
        i, j = 0, 0
        if strs == [] or strs[0] == "":
            return LCP
        else:
            LCP_temp = strs[0][j]
        while True:
            if i == len(strs):
                i = 0
                LCP += LCP_temp
                if j == len(strs[0]) - 1:
                    return LCP
                else:
                    j += 1
                    LCP_temp = strs[0][j]
                    continue
            if re.match(LCP_temp, strs[i][len(LCP):]):
                i += 1
            else:
                return LCP

solution = Solution()
result = solution.longestCommonPrefix(["aa","aa"])
print(result)
print(type(result))